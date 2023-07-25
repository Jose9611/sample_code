# Generated by Django 3.0.1 on 2023-07-11 16:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0008_auto_20230711_1611'),
    ]

    operations = [
        migrations.AddField(
            model_name='flat',
            name='apartment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='flat_apartment', to='book.Apartment'),
        ),
    ]
