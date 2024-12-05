from pydantic import BaseModel
from tortoise.contrib.pydantic import pydantic_model_creator
from core.models.medicine import Medicine
from core.models.store import Store
from typing import Optional

class MedicinePayload(BaseModel):
    name : str
    # location : Optional[str]


Medicine_Pydantic = pydantic_model_creator(Medicine,name="Medicine")
Medicine_InPydantic = pydantic_model_creator(Medicine,name="MedicineIn",exclude=('id','store'))

Store_Pydantic = pydantic_model_creator(Store,name="Store")
Store_InPydantic = pydantic_model_creator(Store,name="StoreIn",exclude=('store_owner_name'))