from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# dummy database URL 
db_url = "postgresql://username:password@localhost:5432/database_name"

engine = create_engine(db_url)

SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



























