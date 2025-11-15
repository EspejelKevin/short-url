from pydantic import BaseModel


class Response(BaseModel):
    data: dict
    meta: dict
    status_code: int = 500
