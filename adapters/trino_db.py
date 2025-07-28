import trino

def get_trino_connection():
    conn = trino.dbapi.connect(
        host = "trino",
        port = 8080,
        user = "admin",
        catalog = "postgresql",
        schema = "public"
    )
    return conn

def run_trino_query(query: str):
    conn = get_trino_connection()
    cur = conn.cursor()
    cur.execute(query)
    return cur.fetchall()