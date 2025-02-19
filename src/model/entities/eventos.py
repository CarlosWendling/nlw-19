from src.model.configs.base import Base
from sqlalchemy import Column, String, Integer #type: ignore

class Eventos (Base):
    __tablename__ = "Eventos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String)

