from fastapi import APIRouter,Depends
from app.shemas import User,UserId,ShowUser
from app.db.database import get_db 
from sqlalchemy.orm import Session 
from app.db import models 


router = APIRouter( 
 prefix="/user",
tags=["Users"]
)


usuarios=[]
#obtener  usuario
#@router.get('/',response_model=List[ShowUser])
@router.get('/')
def obtener_usuarios(db:Session= Depends(get_db)): 
  data= db.query(models.User).all() 
  return data


#crear usuario
@router.post('/')
def Crear_usuario (user:User,db:Session= Depends(get_db)):
  usuario = user.dict()
 
  nuevo_usuario = models.User( 
   username=usuario["username"],
   password=usuario["password"], 
   nombre=usuario["nombre"], 
   apellido=usuario["apellido"], 
   direccion=usuario["direccion"],
   telefono=usuario["telefono"], 
   correo=usuario["correo"],
   )
  db.add(nuevo_usuario) 
  db.commit() 
  db.refresh(nuevo_usuario)
  return {"respuesta": "usuario creado"}

#obtener_usuario
@router.post('/{user_id}') 
def obtener_usuario (user_id:int, db:Session= Depends(get_db)):
 usuario =db.query(models.User).filter(models.User.id == user_id).first()
 if not usuario: 
    return {"respuesta": "usuario no encontrado"}
 return usuario


#eliminar_usuario
@router.delete('/')
def eliminar_usuario (user_id:int, db:Session= Depends(get_db)):  
 usuario =db.query(models.User).filter(models.User.id == user_id)
 if not usuario: 
    return {"respuesta": "usuario no encontrado"} 
 usuario.delete(synchronize_session=False)
 db.commit() 
 return {"respuesta": "eliminado correctamente"}



#actualizar_usuario 
@router.put('/{user_id}')
def actualizar_usuario (user_id:int, updateUser:User): 
 for index,user in enumerate (usuarios): 
  if user["id"] == user_id:
   usuarios[index]["id"] = updateUser.dict()["id"]
   usuarios[index]["nombre"] = updateUser.dict()["nombre"]
   usuarios[index]["apellido"] = updateUser.dict()["apellido"] 
   usuarios[index]["direccion"] = updateUser.dict()["direccion"] 
   usuarios[index]["telefono"] = updateUser.dict()["telefono"] 
   return {"respuesta": "usuario actualizado"}
  return {"respuesta": "usuario no encontrado"}