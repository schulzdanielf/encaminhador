# Generated by Django 3.1.4 on 2021-01-28 18:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alarmes', '0004_auto_20210128_1207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='Ambiente',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='evento',
            name='OpenTime',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 28, 15, 18, 21, 147202), editable=False),
        ),
        migrations.AlterField(
            model_name='evento',
            name='UpdateTime',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 28, 15, 18, 21, 147293), editable=False),
        ),
        migrations.AlterField(
            model_name='incidente',
            name='OpenTime',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 28, 15, 18, 21, 148522), editable=False),
        ),
        migrations.AlterField(
            model_name='incidente',
            name='UpdateTime',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 28, 15, 18, 21, 148602), editable=False),
        ),
        migrations.AlterField(
            model_name='incidente',
            name='data_evento',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 28, 15, 18, 21, 148622), editable=False),
        ),
    ]
