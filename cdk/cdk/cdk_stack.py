from aws_cdk import (
    # Duration,
    Stack,
    aws_s3 as s3,
    aws_s3_deployment as s3deploy,
    aws_cloudfront as cloudfront,
    aws_cloudfront_origins as cloudfront_origins,
    aws_lambda as _lambda,
    aws_apigateway as apigateway,
    Duration,
    RemovalPolicy,
    Aws
    # aws_sqs as sqs,
)
import os
import re
from dotenv import load_dotenv
from constructs import Construct

class CdkStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        load_dotenv()

        # Backend 
        docker_lambda = _lambda.DockerImageFunction(self, "MovieReviewSentimentAnalysisLambda",
                                                    code=_lambda.DockerImageCode.from_image_asset(os.path.join('..', 'backend')),
                                                    timeout=Duration.seconds(30)
                                                    )
        
        # API Gateway
        api = apigateway.LambdaRestApi(self, "MovieReviewSentimentAnalysisAPI",
                                       handler=docker_lambda,
                                       proxy=True,
                                       description="Movie Review Sentiment Analysis API"
                                       )

        # Frontend
        bucket = s3.Bucket(self, "MovieReviewSentimentAnalysisFrontend",
                           #website_index_document="index.html",
                           #website_error_document ="index.html",
                           bucket_name= os.getenv('FE_BUCKET_NAME'),
                           public_read_access=False,
                           removal_policy=RemovalPolicy.DESTROY,
                           auto_delete_objects=True)
        oai = cloudfront.OriginAccessIdentity(self, "MovieReviewSentimentAnalysisOriginAccessIdentity")
        #bucket.grant_read(origin_access_id)
        

        distribution = cloudfront.Distribution(self, "MovieReviewSentimentAnalysisDistribution",
                                               default_root_object="index.html",
                                               error_responses=[
                                                   cloudfront.ErrorResponse(
                                                         http_status=403,
                                                         response_http_status=200,
                                                         response_page_path="/index.html",
                                                         ttl=Duration.seconds(0)
                                                    ),
                                                    cloudfront.ErrorResponse(
                                                         http_status=404,
                                                         response_http_status=200,
                                                         response_page_path="/index.html",
                                                         ttl=Duration.seconds(0)
                                                    )
                                               ],
                                               default_behavior=cloudfront.BehaviorOptions(
                                                   origin=cloudfront_origins.S3BucketOrigin.with_origin_access_identity(bucket, origin_access_identity=oai),
                                                   allowed_methods=cloudfront.AllowedMethods.ALLOW_ALL,
                                                   cached_methods=cloudfront.CachedMethods.CACHE_GET_HEAD,
                                                   viewer_protocol_policy=cloudfront.ViewerProtocolPolicy.REDIRECT_TO_HTTPS),                                                   
                                                   geo_restriction=cloudfront.GeoRestriction.allowlist('US', 'CA', 'GB')
                                               )
        distribution.add_behavior("/api/*", cloudfront_origins.HttpOrigin(os.getenv('API_GATEWAY_URL')),  
                                  allowed_methods=cloudfront.AllowedMethods.ALLOW_ALL,
                                  #cached_methods=cloudfront.CachedMethods.CACHE_NONE,
                                  viewer_protocol_policy=cloudfront.ViewerProtocolPolicy.REDIRECT_TO_HTTPS)
        
        bucket.grant_read(oai)


        
        self.api_url = api.url
        self.bucket_name = bucket.bucket_name
        self.distribution_id = distribution.distribution_id