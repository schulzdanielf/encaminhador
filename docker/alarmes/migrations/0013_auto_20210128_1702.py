# Generated by Django 3.1.4 on 2021-01-28 20:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alarmes', '0012_auto_20210128_1643'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evento',
            name='action',
        ),
        migrations.RemoveField(
            model_name='incidente',
            name='action',
        ),
        migrations.AlterField(
            model_name='evento',
            name='OpenTime',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 28, 17, 2, 46, 912285), editable=False),
        ),
        migrations.AlterField(
            model_name='evento',
            name='UpdateTime',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 28, 17, 2, 46, 912378), editable=False),
        ),
        migrations.AlterField(
            model_name='incidente',
            name='OpenTime',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 28, 17, 2, 46, 912946)),
        ),
        migrations.AlterField(
            model_name='incidente',
            name='UpdateTime',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 28, 17, 2, 46, 913026)),
        ),
        migrations.AlterField(
            model_name='incidente',
            name='data_evento',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 28, 17, 2, 46, 913048)),
        ),
    ]
