from typing import List
from fastapi import FastAPI
from fastapi.routing import APIRouter
from mangum import Mangum
from dotenv import load_dotenv
import uvicorn

from app.models.Movie import Movie
from app.models.Review import Review
from app.models.ReviewsRequest import ReviewsRequest

from app.services.MovieSearch import MovieSearch
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
# Load environment variables from .env file
load_dotenv()

api_router = APIRouter()

@api_router.get("/hello")
def read_root():
    return {"Hello": "World"}

@api_router.get("/movie", response_model=List[Movie])
def get_movie(q: str):
    search = MovieSearch()
    results = search.search(q)
    print(results)
    return JSONResponse(content=jsonable_encoder(results))

@api_router.post("/reviews", response_model=List[Review])
def get_reviews(request: ReviewsRequest):
    search = MovieSearch()
    reviews = search.get_reviews(request.url)
    return JSONResponse(content=jsonable_encoder(reviews))


app = FastAPI()
app.include_router(api_router, prefix='/api')  # Include your router here

# This is the entry point for the AWS Lambda function.
handler = Mangum(app)

# The following code is for local testing. It will not be executed in AWS Lambda.

if __name__ == '__main__':
    uvicorn.run('main:app', port=5000)