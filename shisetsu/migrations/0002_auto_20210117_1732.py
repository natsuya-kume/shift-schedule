# Generated by Django 3.1.5 on 2021-01-17 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shisetsu', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shisetsu',
            name='fax',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='FAX番号'),
        ),
        migrations.AlterField(
            model_name='shisetsu',
            name='tel',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='電話番号'),
        ),
    ]
