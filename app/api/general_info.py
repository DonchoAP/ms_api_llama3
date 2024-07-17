from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas
from ..database import get_db
from ..llama import llama

router = APIRouter()

@router.get("/general-info", response_model=schemas.GeneralInfo)
def read_general_info(db: Session = Depends(get_db)):
    general_info = crud.get_general_info(db)
    if general_info is None:
        raise HTTPException(status_code=404, detail="General info not found")
    return general_info

@router.post("/general-info", response_model=schemas.GeneralInfo)
def create_general_info(general_info: schemas.GeneralInfoCreate, db: Session = Depends(get_db)):
    return crud.create_general_info(db=db, general_info=general_info)

@router.get("/general-info/summary")
def get_general_info_summary(db: Session = Depends(get_db)):
    general_info = crud.get_general_info(db)
    if general_info is None:
        raise HTTPException(status_code=404, detail="General info not found")
    
    prompt = f"Summarize this information about Multiple Sclerosis: {general_info.definition}"
    summary = llama.generate_response(prompt)
    
    return {"summary": summary}