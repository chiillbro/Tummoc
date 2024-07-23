from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Base, Teacher, Student, engine, SessionLocal

app = FastAPI()

Base.metadata.create_all(bind=engine)

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def read_root():
    return {"message": "Hello World"}

@app.post("/teachers/")
def create_teacher(name: str, subject: str, db: Session = Depends(get_db)):
    teacher = Teacher(name=name, subject=subject)
    db.add(teacher)
    db.commit()
    db.refresh(teacher)
    return teacher

@app.get("/teachers/")
def read_teachers(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    teachers = db.query(Teacher).offset(skip).limit(limit).all()
    return teachers

@app.post("/students/")
def create_student(name: str, age: int, teacher_id: int, db: Session = Depends(get_db)):
    student = Student(name=name, age=age, teacher_id=teacher_id)
    db.add(student)
    db.commit()
    db.refresh(student)
    return student

@app.get("/students/")
def read_students(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    students = db.query(Student).offset(skip).limit(limit).all()
    return students

@app.post("/assign-student/")
def assign_student_to_teacher(student_id: int, teacher_id: int, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    student.teacher_id = teacher_id
    db.commit()
    return student
