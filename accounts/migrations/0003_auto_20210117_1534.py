# Generated by Django 3.1.5 on 2021-01-17 06:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_staff_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staff',
            name='name',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='password',
        ),
    ]