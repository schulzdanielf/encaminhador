# Generated by Django 3.1.4 on 2021-01-28 19:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alarmes', '0008_auto_20210128_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='OpenTime',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 28, 16, 12, 53, 847399), editable=False),
        ),
        migrations.AlterField(
            model_name='evento',
            name='UpdateTime',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 28, 16, 12, 53, 847475), editable=False),
        ),
        migrations.AlterField(
            model_name='incidente',
            name='OpenTime',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 28, 16, 12, 53, 848582)),
        ),
        migrations.AlterField(
            model_name='incidente',
            name='UpdateTime',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 28, 16, 12, 53, 848655)),
        ),
        migrations.AlterField(
            model_name='incidente',
            name='data_evento',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 28, 16, 12, 53, 848673)),
        ),
    ]