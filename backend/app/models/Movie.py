from pydantic import BaseModel, Field

class Movie(BaseModel):
    title: str
    year: int
    cast: str
    url: str