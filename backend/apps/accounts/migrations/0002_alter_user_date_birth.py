# Generated by Django 3.2.9 on 2022-06-08 15:23

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date_birth',
            field=models.DateField(default=datetime.datetime(2022, 6, 8, 15, 23, 10, 130709, tzinfo=utc), verbose_name='Дата рождения'),
        ),
    ]