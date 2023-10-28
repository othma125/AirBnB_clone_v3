#!/usr/bin/python3
""" holds class User"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from hashlib import md5


class User(BaseModel, Base):
    """Representation of a user """
    if models.storage_t == 'db':
        __tablename__ = 'users'
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship("Place", backref="user")
        reviews = relationship("Review", backref="user")
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""

    def __init__(self, *args, **kwargs):
        """initializes user"""
        if kwargs:
            if "password" in kwargs:
                encoded = kwargs["password"].encode()
                kwargs.updates({"password": md5(encoded).hexdigest()})
            super().__init__(*args, **kwargs)

    def to_dict(self, save_password=False):
        """Return dictionary representation of User instance"""
        new_dict = super().to_dict()
        if not save_password:
            new_dict.pop("password", None)
        return new_dict

    @property.getter
    def password(self):
        """Getter for password"""
        return self.__password

    @password.setter
    def password(self, value):
        """Setter for password"""
        self.__password = md5(value.encode()).hexdigest()

    def save(self):
        """Save User instance"""
        self.password = self.__password
        super().save()
