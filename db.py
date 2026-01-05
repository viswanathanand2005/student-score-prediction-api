import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from tables import Base

#Loading the environment tables
load_dotenv()

DATABASE_URL = (
    f"mysql+pymysql://{os.getenv('USER')}:"
    f"{os.getenv('PASSWORD')}@"
    f"{os.getenv('HOST')}:3306/"
    f"{os.getenv('DB')}"
)

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    echo=False
)

SessonLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False
)

def get_db():
    db = SessonLocal()
    try:
        yield db
    finally:
        db.close()

Base.metadata.create_all(bind=engine)