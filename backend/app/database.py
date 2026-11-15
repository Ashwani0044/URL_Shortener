import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from urllib.parse import quote_plus

load_dotenv()

password = quote_plus(os.getenv("DB_PASSWORD"))
DATABASE_URL = (
    f"mysql+pymysql://{os.getenv('DB_USER')}:{password}@"
    f"{os.getenv('DB_HOST')}:3306/{os.getenv('DB_NAME')}"
)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
