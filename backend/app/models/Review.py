from pydantic import BaseModel, Field

class Review(BaseModel):
    id: int
    content: str