from sqlalchemy import create_engine

def test_x():
    cnx_str = "postgres://postgres_user:postgres_password@postgres:5432/db_test"
    engine = create_engine(cnx_str)

    with engine.connect() as con:
        rows = con.execute("SELECT table_name FROM information_schema.tables")
        assert len(rows) > 1
