from typing import Optional
from pydantic import BaseModel

class Post(BaseModel):
    title: str
    content: str
    published: bool = True 
    rating: Optional[int] = None
    
class PostCreate(Post):
    pass

class PostUpdate(Post):
    pass
