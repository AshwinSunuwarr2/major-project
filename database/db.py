from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

password = ""
db_url = f"mysql+pymysql://root:{password}@localhost:3306/mydb"

engine = create_engine(db_url)
Base = declarative_base()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
