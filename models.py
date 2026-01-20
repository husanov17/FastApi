from database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, DateTime, Date, ForeginKey
from datetime import datetime, date
from typing import List

class User(Base):
    __tablename__="users"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(100))
    last_name: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(100), unique=True)
    username: Mapped[str] = mapped_column(String(100), unique=True)
    birth_date: Mapped[date] = mapped_column(Date, nullable=True)
    password: Mapped[str] = mapped_column(String(200))
    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    profile: Mapped["Profile"] = relationship(back_populates="user")
    
    
class Profile(Base):
    __tablename__ = "profiles"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    bio: Mapped[int] = mapped_column(String(500))
    user_id = Mapped[int] = mapped_column(ForeginKey("users.id"), unique=True)
    
    user: Mapped["User"] = relationship(back_populates="profile", uselist=False)
    books: Mapped[List["Book"]] = relationship(back_populates="author")
    
class Book(Base):
    __tablename__="books"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    author_id: Mapped[str] = mapped_column(ForeginKey("profiles.id"))
        
    author: Mapped["Profile"] = relationship(back_populates="book")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#class Student(Base):
    __tablename__ = "students"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    birth_date: Mapped[date] = mapped_column(DateTime, nullable=True)
    
 #   courses: Mapped["StudentCourse"] = relationship(back_populates="student")
    
    
    class Course(Base):
        __tablename__ = "courses"
        
        id: Mapped[int] = mapped_column(primary_key=True)
        name: Mapped[str] = mapped_column(String(100))
       # price: Mapped[float] = mapped_column(DECIMAL(10, 2))
        
   #     Students: Mapped['StudentCourse'] = relationship(back_population())
    
    