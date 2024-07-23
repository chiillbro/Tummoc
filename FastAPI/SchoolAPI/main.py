from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from models import Base, Teacher, Student, engine, SessionLocal

app = FastAPI()

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Pydantic models
class TeacherCreate(BaseModel):
    name: str
    subject: str

class StudentCreate(BaseModel):
    name: str
    age: int
    teacher_id: int

class AssignStudent(BaseModel):
    student_id: int
    teacher_id: int

@app.get("/")
async def read_root():
    return {"message": "Hello World"}

# create teacher
@app.post("/teachers/")
def create_teacher(teacher: TeacherCreate, db: Session = Depends(get_db)):
    new_teacher = Teacher(name=teacher.name, subject=teacher.subject)
    db.add(new_teacher)
    db.commit()
    db.refresh(new_teacher)
    return new_teacher

# read all teachers
@app.get("/teachers/")
def read_teachers(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    teachers = db.query(Teacher).offset(skip).limit(limit).all()
    return teachers

# create student
@app.post("/students/")
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    new_student = Student(name=student.name, age=student.age, teacher_id=student.teacher_id)
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student

# read all students
@app.get("/students/")
def read_students(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    students = db.query(Student).offset(skip).limit(limit).all()
    return students

# assign student to teacher
@app.post("/assign-student/")
def assign_student_to_teacher(assign_data: AssignStudent, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.id == assign_data.student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    student.teacher_id = assign_data.teacher_id
    db.commit()
    return student
