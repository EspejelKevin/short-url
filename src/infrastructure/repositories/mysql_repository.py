from domain import DBRepository, ShorterDTO


class MySQLRepository(DBRepository):
    def __init__(self, db_factory) -> None:
        self.db_factory = db_factory

    def get_url_by_id(self, id: str) -> ShorterDTO:
        with self.db_factory() as db:
            session = db.get_session()
            cursor = session.cursor()
            query = 'SELECT * FROM shorter WHERE id=%s'
            data = (id,)
            cursor.execute(query, data)
            shorter = cursor.fetchone()
            return ShorterDTO(id=shorter[0], url=shorter[1], code=shorter[2])

    def get_url_by_code(self, code: str) -> ShorterDTO:
        with self.db_factory() as db:
            session = db.get_session()
            cursor = session.cursor()
            query = 'SELECT * FROM shorter WHERE code=%s'
            data = (code,)
            cursor.execute(query, data)
            shorter = cursor.fetchone()
            return ShorterDTO(id=shorter[0], url=shorter[1], code=shorter[2])
        
    def get_shorter_by_url(self, url: str) -> ShorterDTO:
        with self.db_factory() as db:
            session = db.get_session()
            cursor = session.cursor()
            query = 'SELECT * FROM shorter WHERE url=%s'
            data = (url,)
            cursor.execute(query, data)
            shorter = cursor.fetchone()
            return ShorterDTO(id=shorter[0], url=shorter[1], code=shorter[2])
        
    def create_shorter(self, shorter: ShorterDTO) -> bool:
        try:
            with self.db_factory() as db:
                session = db.get_session()
                cursor = session.cursor()
                query = 'INSERT INTO shorter VALUES(%s, %s, %s)'
                data = (shorter.id, shorter.url, shorter.code)
                cursor.execute(query, data)
                return cursor.rowcount > 0
        except Exception:
            return False
        
    def update_shorter(self, shorter: ShorterDTO) -> bool:
        try:
            with self.db_factory() as db:
                session = db.get_session()
                cursor = session.cursor()
                query = 'UPDATE shorter set url=%s, code=%s'
                data = (shorter.url, shorter.code)
                cursor.execute(query, data)
                return cursor.rowcount > 0
        except Exception:
            return None
        
    def delete_shorter(self, id: str) -> bool:
        try:
            with self.db_factory() as db:
                session = db.get_session()
                cursor = session.cursor()
                query = 'DELETE FROM shorter WHERE id=%s'
                data = (id,)
                cursor.execute(query, data)
                return cursor.rowcount > 0
        except Exception:
            return False
