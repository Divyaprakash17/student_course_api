from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class CourseBase(BaseModel):
    title: str
    description: Optional[str] = None

class CourseCreate(CourseBase):
    pass

class CourseOut(CourseBase):
    id: int
    class Config:
        orm_mode = True

class StudentBase(BaseModel):
    name: str
    email: str

class StudentCreate(StudentBase):
    pass

class StudentOut(StudentBase):
    id: int
    courses: List[CourseOut] = []
    class Config:
        orm_mode = True

class Enroll(BaseModel):
    student_id: int
    course_id: int
