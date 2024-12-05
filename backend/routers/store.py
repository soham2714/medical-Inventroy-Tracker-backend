from fastapi import APIRouter, HTTPException,Form
from fastapi.requests import Request

from typing import Optional
from core.models.store import Store
from core.schemas.schema import Store_Pydantic, Store_InPydantic

router = APIRouter(
    prefix="/store",
    tags=["Store"]
)


@router.get("/")
async def do_nothing():
    return {"msg":"Works"}

@router.post("/signup")
async def create_store(storeName :str = Form(...), address : str = Form(...), storeOwnerName : str = Form(...)):
    
    data = await Store.filter(store_name=storeName,location=address,store_owner_name=storeOwnerName).first()
    
    if data:
        raise HTTPException(409,detail="Store already exists")
    
    new_store = await Store.create(store_name=storeName,location=address,store_owner_name=storeOwnerName)
    
    return await Store_Pydantic.from_tortoise_orm(new_store)

@router.post("/verify")
async def verify_store_owner(licenseNumber: str = Form(...), storeName:str = Form(...),storeOwnerName : Optional[str] = Form(None)):
    
    return await Store_Pydantic.from_queryset_single(Store.get(store_id=int(licenseNumber),store_name=storeName,store_owner_name=storeOwnerName))
    
@router.get("/medicine")
async def fetch_medicine_of_store(request:Request):
    
    store_id = request.query_params.get("store_id")

    if not store_id:
        raise HTTPException(403,detail="Invalid argument")
    
    return await Store_InPydantic.from_queryset(Store.filter(store_id=store_id).all())