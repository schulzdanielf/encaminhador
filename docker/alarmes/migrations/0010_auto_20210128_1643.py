# Generated by Django 3.1.4 on 2021-01-28 19:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alarmes', '0009_auto_20210128_1612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='OpenTime',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 28, 16, 43, 18, 448295), editable=False),
        ),
        migrations.AlterField(
            model_name='evento',
            name='UpdateTime',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 28, 16, 43, 18, 448387), editable=False),
        ),
        migrations.AlterField(
            model_name='incidente',
            name='OpenTime',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 28, 16, 43, 18, 449662)),
        ),
        migrations.AlterField(
            model_name='incidente',
            name='UpdateTime',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 28, 16, 43, 18, 449739)),
        ),
        migrations.AlterField(
            model_name='incidente',
            name='data_evento',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 28, 16, 43, 18, 449771)),
        ),
    ]