# Generated by Django 4.1.5 on 2023-02-07 21:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("LittleLemonAPI", "0002_alter_booking_bookingdate"),
    ]

    operations = [
        migrations.AlterField(
            model_name="booking",
            name="BookingDate",
            field=models.DateField(
                default=datetime.datetime(2023, 2, 8, 4, 32, 48, 717345)
            ),
        ),
    ]
