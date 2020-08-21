from sqlalchemy import create_engine

def test_x():
    cnx_str = "postgres://postgres:postgres_password@postgres:5432/postgres"
    engine = create_engine(cnx_str)

    with engine.connect() as con:
        rows = con.execute("SELECT table_name FROM information_schema.tables")
        assert len(rows) > 1
