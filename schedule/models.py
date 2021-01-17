from django.db import models
from shisetsu.models import *
from accounts.models import *
from django.contrib.auth import get_user_model


# Create your models here.

class Shift(models.Model):
    id = models.AutoField(verbose_name='シフトID',primary_key=True)
    name = models.CharField(verbose_name='シフト名', max_length=1)
    start_time = models.TimeField(verbose_name="開始時間")
    end_time = models.TimeField(verbose_name="終了時間")
    wrok_time = models.IntegerField(verbose_name='勤務時間')

    def __str__(self):
        return self.name

class Schedule(models.Model):
    id = models.AutoField(verbose_name='スケジュールID',primary_key=True)
    # user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    user=models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    date = models.DateField(verbose_name='日付')
    shift_name_1 = models.ForeignKey(Shift, verbose_name='1シフト名', related_name='shift_name1',on_delete=models.SET_NULL,null= True)
    shisetsu_name_1 = models.ForeignKey(Shisetsu, verbose_name='1施設', related_name='shisetsu_name1',on_delete=models.SET_NULL,blank=True, null=True)
    shift_name_2 = models.ForeignKey(Shift, verbose_name='2シフト名', related_name='shift_name2',on_delete=models.SET_NULL,blank=True, null=True)
    shisetsu_name_2 = models.ForeignKey(Shisetsu, verbose_name='2施設', related_name='shisetsu_name2',on_delete=models.SET_NULL,blank=True, null=True)
    shift_name_3 = models.ForeignKey(Shift, verbose_name='3シフト名', related_name='shift_name3',on_delete=models.SET_NULL,blank=True, null=True)
    shisetsu_name_3 = models.ForeignKey(Shisetsu, verbose_name='3施設', related_name='shisetsu_name3',on_delete=models.SET_NULL,blank=True, null=True)
    shift_name_4 = models.ForeignKey(Shift, verbose_name='4シフト名', related_name='shift_name4',on_delete=models.SET_NULL,blank=True, null=True)
    shisetsu_name_4 = models.ForeignKey(Shisetsu, verbose_name='4施設', related_name='shisetsu_name4',on_delete=models.SET_NULL,blank=True, null=True)
    
