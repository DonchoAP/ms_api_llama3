from sqlalchemy.orm import Session
from . import models, schemas

def get_general_info(db: Session):
    return db.query(models.GeneralInfo).first()

def create_general_info(db: Session, general_info: schemas.GeneralInfoCreate):
    db_general_info = models.GeneralInfo(**general_info.dict())
    db.add(db_general_info)
    db.commit()
    db.refresh(db_general_info)
    return db_general_info

def get_symptoms(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Symptom).offset(skip).limit(limit).all()

def create_symptom(db: Session, symptom: schemas.SymptomCreate):
    db_symptom = models.Symptom(**symptom.dict())
    db.add(db_symptom)
    db.commit()
    db.refresh(db_symptom)
    return db_symptom

# Similar CRUD functions for statistics, treatments, and research advances...