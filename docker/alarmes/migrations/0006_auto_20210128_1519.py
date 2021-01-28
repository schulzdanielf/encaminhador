# Generated by Django 3.1.4 on 2021-01-28 18:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alarmes', '0005_auto_20210128_1518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='OpenTime',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 28, 15, 19, 47, 732136), editable=False),
        ),
        migrations.AlterField(
            model_name='evento',
            name='UpdateTime',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 28, 15, 19, 47, 732235), editable=False),
        ),
        migrations.AlterField(
            model_name='incidente',
            name='Ambiente',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='incidente',
            name='OpenTime',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 28, 15, 19, 47, 733601), editable=False),
        ),
        migrations.AlterField(
            model_name='incidente',
            name='UpdateTime',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 28, 15, 19, 47, 733682), editable=False),
        ),
        migrations.AlterField(
            model_name='incidente',
            name='data_evento',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 28, 15, 19, 47, 733702), editable=False),
        ),
    ]
