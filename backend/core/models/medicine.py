import datetime
from tortoise.models import Model
from tortoise import fields


class Medicine(Model):

    id = fields.BigIntField(pk=True)
    medicine_name = fields.CharField(max_length=300)
    manufacturer = fields.CharField(max_length=300)
    price = fields.IntField(null=False)
    quantity = fields.IntField(null=False)
    expires_at = fields.DatetimeField(default=datetime.datetime.utcnow())
    store = fields.ForeignKeyField(model_name="models.Store",null=False)

    class Meta:
        table = "medicine"
        unique_together = ('id','store')


    # class PydanticMeta:
    #     exclude = ("owner",)