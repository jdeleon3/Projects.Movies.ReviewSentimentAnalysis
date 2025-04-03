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
    RemovalPolicy
    # aws_sqs as sqs,
)
import os
from dotenv import load_dotenv
from constructs import Construct

class CdkStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        load_dotenv()

        # Frontend
        bucket = s3.Bucket(self, "MovieReviewSentimentAnalysisFrontend",
                           website_index_document="index.html",
                           bucket_name= os.getenv('FE_BUCKET_NAME'),
                           public_read_access=False,
                           removal_policy=RemovalPolicy.DESTROY,
                           auto_delete_objects=True)
        #origin_access_id = cloudfront.OriginAccessIdentity(self, "MovieReviewSentimentAnalysisOriginAccessIdentity")
        #bucket.grant_read(origin_access_id)

        distribution = cloudfront.Distribution(self, "MovieReviewSentimentAnalysisDistribution",
                                               default_root_object="index.html",
                                               default_behavior=cloudfront.BehaviorOptions(
                                                   origin=cloudfront_origins.S3StaticWebsiteOrigin(bucket),
                                                   viewer_protocol_policy=cloudfront.ViewerProtocolPolicy.REDIRECT_TO_HTTPS),
                                                   allow_methods=cloudfront.AllowedMethods.ALLOW_ALL,
                                                   geo_restriction=cloudfront.GeoRestriction.allow_list('US', 'CA', 'GB')
                                               )
        bucket.grant_read(distribution.grant_principal)
        

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
        
        self.api_url = api.url
        self.bucket_name = bucket.bucket_name
        self.distribution_id = distribution.distribution_id