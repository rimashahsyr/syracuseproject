# Generated by Django 2.2.6 on 2019-12-17 00:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Events', '0019_auto_20191216_0915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventinfo',
            name='EventLocation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NearbyEvents.LocationPreferences'),
        ),
    ]
