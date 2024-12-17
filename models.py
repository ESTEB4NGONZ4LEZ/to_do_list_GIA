# models.py
from sqlalchemy import Column, Integer, String, Boolean
from database import base

class Tarea(base):
    __tablename__ = 'tareas'

    id          = Column(Integer, primary_key = True, index = True)
    titulo      = Column(String, index = True)
    descripcion = Column(String)
    completada  = Column(Boolean, default = False)
