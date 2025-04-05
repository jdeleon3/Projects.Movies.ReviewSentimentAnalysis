from pydantic import BaseModel, Field

class ReviewsRequest(BaseModel):
    url: str