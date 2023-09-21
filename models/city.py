#!/usr/bin/python3
"""Inheits from the BaseModel class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey


class City(BaseModel, Base):
    """city class"""
    __tablename__ = "cities"
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)
