# Generated by Django 3.0.1 on 2023-07-11 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0006_booking_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='apartment',
            name='region_id',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='region_id',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]
