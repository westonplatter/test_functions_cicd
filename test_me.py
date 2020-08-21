from os import environ

from sqlalchemy import create_engine

def test_x():
    cnx_str = environ.get("TEST_DATABASE_URL")
    engine = create_engine(cnx_str)

    with engine.connect() as con:
        result = con.execute("SELECT table_name FROM information_schema.tables")
        rows = [x for x in result]

    assert len(rows) > 5
