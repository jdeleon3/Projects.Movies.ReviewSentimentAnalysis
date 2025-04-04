from fastapi import FastAPI
from fastapi.routing import APIRouter
from mangum import Mangum
import os
from dotenv import load_dotenv
import uvicorn

# Load environment variables from .env file
load_dotenv()

api_router = APIRouter()

@api_router.get("/hello")
def read_root():
    return {"Hello": "World"}

app = FastAPI()
app.include_router(api_router, prefix='/api')  # Include your router here



# Allow CORS for all origins (you can restrict this to specific origins if needed)
# allowed = os.getenv("ALLOWED_ORIGINS", "*")
# if allowed == "*":
#     allowed = ["*"]
# else:
#     allowed = [origin.strip() for origin in allowed.split(',')]
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=[allowed],
#     allow_credentials=True,
#     allow_methods=['get', 'post', 'options'],
#     allow_headers=["*"],
# )




# This is the entry point for the AWS Lambda function.
handler = Mangum(app)

# The following code is for local testing. It will not be executed in AWS Lambda.

if __name__ == '__main__':
    uvicorn.run('main:app', port=5000)