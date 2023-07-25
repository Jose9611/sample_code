# Generated by Django 3.0.1 on 2023-07-25 17:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        ('book', '0010_assignedapartment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Userpermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_type', models.CharField(max_length=30)),
                ('is_permission', models.BooleanField(default=False)),
                ('permission', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.Permission')),
            ],
        ),
        migrations.DeleteModel(
            name='Book',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='booked_by',
        ),
        migrations.AddField(
            model_name='booking',
            name='flat',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='booking_flat', to='book.Flat'),
        ),
    ]
