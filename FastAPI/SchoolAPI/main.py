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
    
class TeacherUpdate(BaseModel):
    name: str
    subject: str

class StudentCreate(BaseModel):
    name: str
    age: int
    teacher_id: int

class StudentUpdate(BaseModel):
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
    
# update teacher
@app.put("/teachers/{teacher_id}")
def update_teacher(teacher_id: int,  teacher_update: TeacherUpdate, db: Session = Depends(get_db)):
    teacher = db.query(Teacher).filter(Teacher.id == teacher_id).first()
    if not teacher:
        raise HTTPException(status_code=404, detail="Teacher not found")
    for key, value in teacher_update.dict().items():
        setattr(teacher, key, value)
    db.commit()
    db.refresh(teacher)
    return teacher

#delete teacher
@app.delete("/teachers/{teacher_id}")
def delete_teacher(teacher_id: int, db: Session = Depends(get_db)):
    teacher = db.query(Teacher).filter(Teacher.id == teacher_id).first()
    if not teacher:
        raise HTTPException(status_code=404, detail="Teacher not found")
    db.delete(teacher)
    db.commit()
    return {"message" : "Teacher deleted"}

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

# update student
@app.put("/students/{student_id}")
def update_student(student_id: int, student_update: StudentUpdate, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    for key, value in student_update.dict().items():
        setattr(student, key, value)
    db.commit()
    db.refresh(student)
    return student

# delete student
@app.delete("/students/{student_id}")
def delete_student(student_id: int, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    db.delete(student)
    db.commit()
    return {"message" : "Student deleted"}

# assign student to teacher
@app.post("/assign-student/")
def assign_student_to_teacher(assign_data: AssignStudent, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.id == assign_data.student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    student.teacher_id = assign_data.teacher_id
    db.commit()
    return student
