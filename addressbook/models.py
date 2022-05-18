from django.db import models
from django.contrib.auth.models import User
from phone_field import PhoneField

# Create your models here.
class Myaddress(models.Model):
    parent = models.ForeignKey(User, on_delete=models.PROTECT,
                               related_name='myaddresss', related_query_name='myaddress')
    fname = models.CharField(max_length=25)
    lname = models.CharField(max_length=25)
    phone = PhoneField(blank=False,help_text='')
    address = models.TextField(blank=True)
    relationship = models.CharField(max_length=50)

    class Meta:
        db_table = 'context_address'