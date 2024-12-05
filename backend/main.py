from fastapi import FastAPI, HTTPException
from starlette.middleware.cors import CORSMiddleware
from database import connect_to_db
from typing import List
import uvicorn

from routers import store
from core.schemas.schema import Medicine_Pydantic,Medicine_InPydantic
from core.models.medicine import Medicine

origins = [
    "http://localhost:3001",
    "http://127.0.0.1:5500",
]

app = FastAPI()
connect_to_db(app=app)

app.include_router(store.router)


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message":"Hello world!"}

@app.get("/medicine",response_model=List[Medicine_Pydantic])
async def fetch_medicine(name:str):
    
    
    return await Medicine_Pydantic.from_queryset(Medicine.filter(medicine_name__icontains=name).all())
    


@app.post("/medicine")
async def create_medicine(payload:Medicine_InPydantic):

    data = payload.model_dump(exclude_unset=True)

    med_obj = await Medicine.create(**data)

    return {
        "data":await Medicine_InPydantic.from_tortoise_orm(med_obj)
    }


@app.put("/medicine")
async def update_medicine(user_payload:Medicine_InPydantic):
    
    data = user_payload.model_dump(exclude_unset=True)

    stored_meds = await Medicine.get(medicine_name=data.get("medicine_name"),store_id=data.get("store_id"))

    if not stored_meds:
        raise HTTPException(404,detail="No such medicine exists in this store")
    
    updated_quantity = stored_meds.quantity + int(data.get("quantity"))

    await Medicine.filter(id=stored_meds.id).update(quantity=updated_quantity)

    return {
        "data":await Medicine_InPydantic.from_queryset_single(Medicine.get(id=stored_meds.id))
    }




if __name__ == "__main__":
    uvicorn.run("main:app",host="localhost",port=4000,reload=True)