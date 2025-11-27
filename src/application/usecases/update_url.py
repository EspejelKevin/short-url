from fastapi.exceptions import HTTPException

from datetime import datetime
import uuid


from domain import DBRepository, ShorterInput, Response, ShorterDTO


class UpdateURL:
    def __init__(self, db_service: DBRepository) -> None:
        self.db_service = db_service
        self.meta = {'transaction_id': str(uuid.uuid4()),
                     'timestamp': datetime.now()}
        
    def execute(self, code: str, shorter: ShorterInput) -> Response:
        shorter_db = self.db_service.get_url_by_code(code)

        if not shorter_db:
            raise HTTPException(404, detail=f'shorter not found: {code}')
        
        new_code = str(uuid.uuid4().int)
        url = shorter.url.encoded_string()
        shorter_dto = ShorterDTO(url=url, code=new_code)

        if not self.db_service.update_shorter(code, shorter_dto):
            raise HTTPException(500, detail='error while updating shorter, try again')

        data = {'url': url, 'new_code': new_code}

        return Response(data=data, meta=self.meta, status_code=200)
