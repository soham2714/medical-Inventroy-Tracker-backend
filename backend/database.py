from tortoise import Tortoise
from tortoise.contrib.fastapi import register_tortoise
from config import settings

def connect_to_db(app):
    register_tortoise(
        app,
        db_url=f'postgres://{settings.db_user}:{settings.db_password}@localhost:5432/medical_inventory_tracker',
        modules={'models': ['core.models.medicine','core.models.store']},
        generate_schemas=True,
        add_exception_handlers=True,
    )

Tortoise.init_models(['core.models.medicine','core.models.store'], "models")

