from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.sql import func
from .database import Base

class GeneralInfo(Base):
    __tablename__ = "general_info"

    id = Column(Integer, primary_key=True, index=True)
    definition = Column(Text, nullable=False)
    last_updated = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

class Symptom(Base):
    __tablename__ = "symptoms"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    description = Column(Text)

class Statistic(Base):
    __tablename__ = "statistics"

    id = Column(Integer, primary_key=True, index=True)
    category = Column(String(100), nullable=False)
    value = Column(String(200), nullable=False)
    year = Column(Integer, nullable=False)

class Treatment(Base):
    __tablename__ = "treatments"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    approval_year = Column(Integer, nullable=False)
    type = Column(String(100))
    description = Column(Text)

class ResearchAdvance(Base):
    __tablename__ = "research_advances"

    id = Column(Integer, primary_key=True, index=True)
    year = Column(Integer, nullable=False)
    title = Column(String(200), nullable=False)
    description = Column(Text)
    source = Column(String(200))