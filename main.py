from fastapi import FastAPI, Depends, HTTPException
from schemas import CreateCustomersRequest,GetCustomersResponse,GetServiceResponse
from sqlalchemy.orm import Session
from database import get_db
from sqlalchemy import select
from models import Customers, Phone, Service, Customers_in_service
from typing import List



app = FastAPI()

@app.post("/customers")
def create(details:CreateCustomersRequest, db: Session = Depends(get_db)):
    ss = db.execute(select(Service).where(Service.service_id.in_(details.service))).scalars()
    if len(list(ss)) != len(details.service):
        raise HTTPException(status_code=400, detail="Говно ввел")
    else:
        to_create = Customers(
            first_name = details.first_name,
            second_name = details.second_name,
            addresses = details.addresses,
            phone = Phone(phone = details.phone)
        )
    db.add(to_create)
    service = details.service
    db.flush()

    for s in service:
        db.add(Customers_in_service(fk_customers_id = to_create.customers_id, fk_service_id = s))
    db.commit()
    return{
        "success": True,
        "created_id": to_create.customers_id
    }

@app.get("/service")
def get_all_service(db: Session = Depends(get_db))-> List[GetServiceResponse]:
    ss = db.execute(select(Service)).scalars()
    # Из схемы если схема не совпадает с базой
    # x = []
    # for s in ss:
    #     x.append(GetServiceResponse(service_id = s.service_id, pay = s.pay))
    return list(ss)

    # Из бд
    # stmt = select(Service)
    # ss = db.execute(stmt).scalars()
    # return list(ss)

@app.get("/customers")
def get_all_customers(db: Session = Depends(get_db))-> List[GetCustomersResponse]:
    rr = db.execute(select(Customers)).scalars()
    return list(rr)


@app.get("/customer")
def get_id(id: int, db: Session = Depends(get_db)) -> GetCustomersResponse: 
    qq = db.query(Customers).filter(Customers.customers_id == id).first()
    return GetCustomersResponse(customers_id = qq.customers_id, first_name = qq.first_name, second_name= qq.second_name, addresses=qq.addresses, phone = qq.phone.phone)

@app.delete("/customers")
def delete(id: int, db: Session = Depends(get_db)): 
    db.query(Phone).filter(Phone.fk_customers_id == id).delete()
    db.query(Customers).filter(Customers.customers_id == id).delete()
    db.commit()
    return{"success": True}