# Generated by Django 3.2.9 on 2021-12-04 08:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Subscrap', '0003_alter_sublist_startdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sublist',
            name='startDate',
            field=models.DateField(default=datetime.datetime(2021, 12, 4, 8, 31, 3, 753477)),
        ),
    ]
