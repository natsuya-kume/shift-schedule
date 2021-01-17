from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

class Staff(models.Model):

    id = models.AutoField(verbose_name='社員ID',primary_key=True)
    name=models.ForeignKey(get_user_model(),on_delete=models.CASCADE,max_length=20,blank=False, null=True,verbose_name='User')
    roll = models.CharField(verbose_name='役職',max_length=10, blank=False, null=True)
    nyushabi = models.DateField(verbose_name='入社日',blank=False, null=True)
    taishabi = models.DateField(verbose_name='退社日',blank=True, null=True)
    hyoujijyun = models.IntegerField(verbose_name='表示順',unique=True)
    jikyu = models.IntegerField(verbose_name='時給',blank=False, null=True)
    delete = models.BooleanField(verbose_name='削除フラグ',default=False)
    create_date = models.DateTimeField(verbose_name='登録日時', auto_now_add=True)
    create_user = models.CharField(verbose_name='登録ユーザ', max_length=50, null=True)
    update_date = models.DateTimeField(verbose_name='更新日時', auto_now=True)
    update_user = models.CharField(verbose_name='更新ユーザ', max_length=50, null=True)

    def __str__(self):
        return str(self.name)