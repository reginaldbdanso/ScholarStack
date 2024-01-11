#!/bin/bash/python3
""" Management class module """
import uuid, datetime, json
from student import Student


class SRMS:
    """SRMS class"""

    students = []
    def __init__(self) -> None:
        with open('students.json', 'r') as f:
            self.students = json.load(f)

    def get_students(self) -> list:
        """get_students method"""
        return self.students

    def get_student_by_id(self, id: str) -> Student:
        """get_student_by_id method"""
        for student in self.students:
            if student.get('id') == id:
                return student
        return None

    def add_student(self, student: Student) -> None:
        """add_student method"""
        self.students.append(student.to_dict())

    def update_student(self, id: str, **kwargs) -> None:
        """update student method"""
        sf = self.get_student_by_id(id)
        if sf is None:
            print('Student not found')
            return
        for key, value in kwargs.items():
            #checking if the key is valid or updatable
            if key not in sf.keys():
                print(f'{key} is Invalid')
                continue
            else:
                sf[key] = value
        sf['updated_at'] = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")

    def delete_student_by_id(self, id: str) -> None:
        """delete student by id method"""
        df = self.get_student_by_id(id)
        if df is None:
            print('Student not found')
            return
        self.students.remove(df)

    def save(self) -> None:
        """save method"""
        with open('students.json', 'w') as f:
            json.dump(self.students, f)

    def __str__(self) -> str:
        """__str__ method"""
        return f'<{self.__class__.__name__} Student Record Management System>'

    def __repr__(self) -> str:
        """__repr__ method"""
        return f'{self.__class__.__name__}()'
