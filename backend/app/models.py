from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

# User table to manage different users (engineers, etc.)
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)

    bom_entries = relationship("SubAssembly", back_populates="uploader")

# Supplier table
class Supplier(Base):
    __tablename__ = 'suppliers'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

# Manufacturer table
class Manufacturer(Base):
    __tablename__ = 'manufacturers'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

# SubAssembly table for BOM entries
class SubAssembly(Base):
    __tablename__ = 'sub_assemblies'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    cost = Column(Integer)
    lead_time = Column(String)
    notes = Column(String)
    supplier_id = Column(Integer, ForeignKey('suppliers.id'))
    manufacturer_id = Column(Integer, ForeignKey('manufacturers.id'))
    uploaded_by_user_id = Column(Integer, ForeignKey('users.id'))

    uploader = relationship("User", back_populates="bom_entries")
