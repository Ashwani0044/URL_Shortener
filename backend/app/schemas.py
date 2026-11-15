from pydantic import BaseModel, HttpUrl

class URLCreate(BaseModel):
    long_url: HttpUrl

class URLResponse(BaseModel):
    id: int
    long_url: str
    short_code: str
    clicks: int

    class Config:
        from_attributes = True