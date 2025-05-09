from sqlalchemy import Column, Integer, String, Text, ForeignKey, Table, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

enrollments = Table(
    'enrollments',
    Base.metadata,
    Column('student_id', ForeignKey('students.id'), primary_key=True),
    Column('course_id', ForeignKey('courses.id'), primary_key=True),
    Column('enrolled_on', DateTime, default=datetime.utcnow)
)

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    courses = relationship('Course', secondary=enrollments, back_populates='students')

class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(Text)
    students = relationship('Student', secondary=enrollments, back_populates='courses')
