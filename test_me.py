from os import environ

from sqlalchemy import create_engine

def test_x():
    u = environ.get("PG_USER")
    p = environ.get("PG_PASSWORD")
    h = environ.get("PG_HOST")
    port = environ.get("PG_PORT")
    db = environ.get("PG_DATABASE")

    cnx_str = f"postgres://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{PG_DATABASE}"
    engine = create_engine(cnx_str)

    with engine.connect() as con:
        rows = con.execute("SELECT table_name FROM information_schema.tables")
        assert len(rows) > 1
