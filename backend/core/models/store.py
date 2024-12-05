from tortoise.models import Model
from tortoise import fields

class Store(Model):
    store_id = fields.BigIntField(pk=True)
    store_name = fields.CharField(max_length=300)
    location = fields.TextField()
    store_owner_name = fields.CharField(max_length=300,null=True)
    
    class Meta:
        table = "store"
        