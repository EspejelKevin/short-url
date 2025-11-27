from pydantic import BaseModel


class ShorterDTO(BaseModel):
    id: str = ''
    url: str = ''
    code: str = ''
