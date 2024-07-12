from app.db.database import Base
from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime


# Definición de la tabla 'users'
class User(Base):
    __tablename__ = "usuario"
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(10), unique=True)
    password = Column(String(10))
    nombre = Column(String(20))
    apellido = Column(String(20))
    direccion = Column(String(30))
    telefono = Column(String(9))  # Cambiado a String para permitir números de teléfono más flexibles
    correo = Column(String(20), unique=True)  # Renombrado a minúsculas para consistencia
    creacion = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    estado = Column(Boolean, default=False)
    ventas = relationship("Venta", backref="usuario", cascade="delete, merge")
 

