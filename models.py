from typing import List
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from database import Base

class Service(Base):
    __tablename__ = "service"
    service_id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    pay: Mapped[int] = mapped_column()
    customers: Mapped[List["Customers"]] = relationship(secondary="customers_in_service",back_populates="service")


class Customers(Base):
    __tablename__ = "customers"
    customers_id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(30))
    second_name: Mapped[str] = mapped_column(String(30))
    addresses: Mapped[str] = mapped_column(String(64))
    service: Mapped[List["Service"]] = relationship(secondary="customers_in_service", back_populates="customers")
    phone: Mapped["Phone"] = relationship(back_populates="customers")

class Phone(Base):
    __tablename__ = "phone"
    phone: Mapped[str] = mapped_column(String(30))
    fk_customers_id: Mapped[int] = mapped_column(ForeignKey("customers.customers_id"),primary_key=True)
    customers: Mapped["Customers"] = relationship(back_populates="phone")

class Customers_in_service(Base):
    __tablename__ = "customers_in_service"
    fk_customers_id: Mapped[int] = mapped_column(ForeignKey("customers.customers_id"),primary_key=True)
    fk_service_id: Mapped[int] = mapped_column(ForeignKey("service.service_id"),primary_key=True)
