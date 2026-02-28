from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URI = "sqlite:///.//todosapp1.db"
#SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:1234@localhost/ToDoApplicationDatabase'
#SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456789@127.0.0.1:3306/ToDoApplicationDatabase'


engine = create_engine(SQLALCHEMY_DATABASE_URI,connect_args={"check_same_thread":False})
#engine = create_engine(SQLALCHEMY_DATABASE_URI)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()