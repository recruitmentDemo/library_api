from pydantic import BaseModel
from typing import Optional

class Book(BaseModel):
    title: str
    author: str
    description: Optional[str] = None
    year_published: Optional[int] = None

class BookUpdate(BaseModel):
    title: Optional[str]
    author: Optional[str]
    description: Optional[str]
    year_published: Optional[int]
