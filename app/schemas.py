from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class GeneralInfoBase(BaseModel):
    definition: str

class GeneralInfoCreate(GeneralInfoBase):
    pass

class GeneralInfo(GeneralInfoBase):
    id: int
    last_updated: datetime

    class Config:
        orm_mode = True

class SymptomBase(BaseModel):
    name: str
    description: Optional[str] = None

class SymptomCreate(SymptomBase):
    pass

class Symptom(SymptomBase):
    id: int

    class Config:
        orm_mode = True

class StatisticBase(BaseModel):
    category: str
    value: str
    year: int

class StatisticCreate(StatisticBase):
    pass

class Statistic(StatisticBase):
    id: int

    class Config:
        orm_mode = True

class TreatmentBase(BaseModel):
    name: str
    approval_year: int
    type: Optional[str] = None
    description: Optional[str] = None

class TreatmentCreate(TreatmentBase):
    pass

class Treatment(TreatmentBase):
    id: int

    class Config:
        orm_mode = True

class ResearchAdvanceBase(BaseModel):
    year: int
    title: str
    description: Optional[str] = None
    source: Optional[str] = None

class ResearchAdvanceCreate(ResearchAdvanceBase):
    pass

class ResearchAdvance(ResearchAdvanceBase):
    id: int

    class Config:
        orm_mode = True