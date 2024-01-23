#!/bin/bash/python3
""" Student class module """
import uuid
import datetime


class Student:
    """Student class"""
    def __init__(self, firstname: str, lastname: str, age: int, gender: str, program: str) -> None:
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.gender = gender
        self.program = program
        self.__id = str(uuid.uuid4())
        self.__created_at = datetime.datetime.utcnow()
        self.updated_at = datetime.datetime.utcnow()

    @property
    def id(self) -> str:
        """getter for id"""
        return self.__id

    @property
    def created_at(self) -> datetime.datetime:
        """getter for created_at"""
        return self.__created_at

    def get_fullname(self) -> str:
        """get_fullname method"""
        return f'{self.firstname} {self.lastname}'

    def to_dict(self) -> dict:
        """returns dictionary representation of the object"""
        obj = {
            'firstname': self.firstname,
            'lastname': self.lastname,
            'age': self.age,
            'gender': self.gender,
            'program': self.program,
            'id': self.id,
            'created_at': self.created_at.strftime("%Y-%m-%d %H:%M:%S"),
            'updated_at': self.updated_at.strftime("%Y-%m-%d %H:%M:%S"),
        }
        return obj

    def __str__(self) -> str:
        """__str__ method"""
        return f'<{self.__class__.__name__} {self.id}>'

    def __repr__(self) -> str:
        """__repr__ method"""
        return f"{self.__class__.__name__}('{self.firstname}', '{self.lastname}', '{self.age}', '{self.gender}', '{self.program}')"
