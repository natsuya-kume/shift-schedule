# Generated by Django 3.1.5 on 2021-01-17 08:21

import colorfield.fields
from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shisetsu',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='施設ID')),
                ('name', models.CharField(max_length=50, verbose_name='施設名')),
                ('adress', models.CharField(max_length=100, verbose_name='住所')),
                ('tel', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, verbose_name='電話番号')),
                ('fax', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, verbose_name='FAX番号')),
                ('color', colorfield.fields.ColorField(default='#FF0000', max_length=18, verbose_name='表示色')),
            ],
        ),
    ]
