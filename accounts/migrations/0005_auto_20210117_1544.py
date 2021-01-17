# Generated by Django 3.1.5 on 2021-01-17 06:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0004_auto_20210117_1543'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staff',
            name='user',
        ),
        migrations.AddField(
            model_name='staff',
            name='name',
            field=models.ForeignKey(max_length=20, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
    ]
