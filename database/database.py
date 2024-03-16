from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHAMY_DATABASE_URL = 'postgresql://postgres:password@localhost:5432/fastapi'

engine = create_engine(SQLALCHAMY_DATABASE_URL)

Base = declarative_base()



SessionLocal = sessionmaker(bind=engine,autocommit=False, autoflush=False)

Base.metadata.create_all(bind=engine)




def get_db():
  db=SessionLocal()
  try:
    yield db
  finally:
    db.close()
  

