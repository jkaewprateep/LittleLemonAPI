# Generated by Django 4.1.5 on 2023-02-07 23:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("LittleLemonAPI", "0009_alter_booking_bookingdate"),
    ]

    operations = [
        migrations.DeleteModel(
            name="MenuItem",
        ),
        migrations.AlterField(
            model_name="booking",
            name="BookingDate",
            field=models.DateField(
                default=datetime.datetime(2023, 2, 8, 6, 21, 5, 931910)
            ),
        ),
    ]
