from fastapi import FastAPI, HTTPException, Depends, status

from pydantic import BaseModel
from typing import Annotated
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()

class IngresoBase(BaseModel):
    carnet:str
    nombrepersona:str

class IngresoBase2(BaseModel):
    idregistro:int
    carnet:str
    nombrepersona:str

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@app.post("/registro/", status_code=status.HTTP_201_CREATED)
async def crear_registro(registro:IngresoBase, db:db_dependency):
    db_registro = models.Ingreso(**registro.dict())
    db.add(db_registro)
    db.commit()
    return "El registro se realizo exitosamente"

