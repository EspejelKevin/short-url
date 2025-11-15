from pydantic import BaseModel, HttpUrl


class ShorterInput(BaseModel):
    url: HttpUrl
