from fastapi import FastAPI 
import uvicorn  
from app.routers import user
from app.db.database import Base,engine
from app.routers import user

def create_tables(): 
  Base.metadata.create_all(bind=engine)

app= FastAPI() 
app.include_router(user.router) 
create_tables()


if __name__== "__main__""":
  uvicorn.run("main.app", port=8000, reload=True)