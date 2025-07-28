from adapters.trino_db import get_trino_connection

class TrinoUserRepository:
    def __init__(self):
        self.conn = get_trino_connection()

    def get_all_users(self):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM users")
        return cur.fetchall()