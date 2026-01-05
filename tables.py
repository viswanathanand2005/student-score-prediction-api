from sqlalchemy import Column,Integer,Float,String,ForeignKey,Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

#Defining the schema of the db tables
class Student(Base):
    __tablename__ = "students"
    
    student_id = Column(Integer,primary_key=True)
    age = Column(Integer)
    gender = Column(String(10))
    parent_education = Column(String(50))

class Academic(Base):
    __tablename__ = 'academic'

    student_id = Column(Integer,ForeignKey('students.student_id'))
    academic_id = Column(Integer,primary_key=True,autoincrement=True)
    attendance_percentage = Column(Float)
    study_hours_per_week = Column(Float)
    assignments_completed = Column(Boolean)
    previous_gpa = Column(Float)

class Performance(Base):
    __tablename__ = 'performance'

    student_id = Column(Integer,ForeignKey('students.student_id'))
    performance_id = Column(Integer,primary_key=True,autoincrement=True)
    final_score = Column(Float)
    pass_status = Column("pass",Boolean)
