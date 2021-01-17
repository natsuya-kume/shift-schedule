from django.db import models
from colorfield.fields import ColorField

# Create your models here.
class Shisetsu(models.Model):
    id = models.IntegerField(verbose_name='施設ID',primary_key=True)
    name = models.CharField(verbose_name='施設名', max_length=50)
    adress = models.CharField(verbose_name='住所', max_length=100)
    tel = models.CharField(verbose_name='電話番号', max_length=20,null=True,blank=True) 
    fax = models.CharField(verbose_name='FAX番号', max_length=20,null=True,blank=True) 
    color = ColorField(verbose_name='表示色', default='#FF0000')