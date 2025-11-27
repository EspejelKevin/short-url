from fastapi.exceptions import HTTPException

from datetime import datetime
import uuid


from domain import DBRepository, Response


class DeleteShorter:
    def __init__(self, db_service: DBRepository) -> None:
        self.db_service = db_service
        self.meta = {'transaction_id': str(uuid.uuid4()),
                     'timestamp': datetime.now()}
        
    def execute(self, code: str) -> Response:
        shorter_db = self.db_service.get_url_by_code(code)

        if not shorter_db:
            raise HTTPException(404, detail=f'shorter not found: {code}')

        if not self.db_service.delete_shorter(code):
            raise HTTPException(500, detail='error while deleting shorter, try again')

        data = {'message': 'shorter deleted with success', 'url': shorter_db.url, 'code': shorter_db.code}

        return Response(data=data, meta=self.meta, status_code=200)
