# Generated by Django 3.2.9 on 2021-12-04 08:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Subscrap', '0002_alter_sublist_startdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sublist',
            name='startDate',
            field=models.DateField(default=datetime.datetime(2021, 12, 4, 8, 27, 22, 308497)),
        ),
    ]
