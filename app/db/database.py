from sqlalchemy import create_engine 
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy.orm import sessionmaker 

# URL de conexión para MySQL usando pymysql
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root@localhost:3306/usuarios"

# Crear la instancia del motor
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Declarative base y sesión
Base = declarative_base()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) 

def get_db(): 
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()