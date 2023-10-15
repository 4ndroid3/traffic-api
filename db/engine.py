from sqlalchemy import create_engine

DATABASE_URL = "postgres://postgres:postgres@localhost/traffic-db"

engine = create_engine(DATABASE_URL)
