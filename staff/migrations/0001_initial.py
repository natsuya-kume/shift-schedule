# Generated by Django 3.1.5 on 2021-01-16 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='社員ID')),
                ('password', models.CharField(max_length=20, verbose_name='パスワード')),
                ('name', models.CharField(max_length=20, null=True, verbose_name='社員氏名')),
                ('roll', models.CharField(max_length=10, null=True, verbose_name='役職')),
                ('nyushabi', models.DateField(null=True, verbose_name='入社日')),
                ('taishabi', models.DateField(null=True, verbose_name='退社日')),
                ('hyoujijyun', models.IntegerField(unique=True, verbose_name='表示順')),
                ('jikyu', models.IntegerField(null=True, verbose_name='時給')),
                ('delete', models.BooleanField(default=False, verbose_name='削除フラグ')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='作成日時')),
                ('create_user', models.IntegerField(max_length=50, null=True, verbose_name='作成ユーザ')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='更新日時')),
                ('update_user', models.IntegerField(max_length=50, null=True, verbose_name='更新ユーザ')),
            ],
        ),
    ]