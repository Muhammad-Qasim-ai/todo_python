from pydantic import BaseModel, Field
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from typing import ClassVar

SQLALCHEMY_DATABASE_URL = "postgresql://username:password@localhost/dbname"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class Todo(BaseModel):
    __tablename__ = "todos"

    id: int = Field(primary_key=True)
    title: str = Column(String, index=True)
    description: str = Column(String, index=True)
    user_id: int = Column(Integer, ForeignKey('users.id'))

    # Define relationship with User model
    user: ClassVar = relationship("User", back_populates="todos")

class User(BaseModel):
    __tablename__ = "users"

    id: int = Field(primary_key=True)
    username: str = Column(String, unique=True, index=True)
    password: str = Column(String)
    
    # Define relationship with Todo model
    todos: ClassVar = relationship("Todo", back_populates="user")
