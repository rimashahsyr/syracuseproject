# Generated by Django 2.0.13 on 2019-12-15 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0005_profileinfo_userpassword'),
        ('Events', '0015_auto_20191204_2014'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventinfo',
            name='Attendee',
            field=models.ManyToManyField(blank=True, to='Profile.ProfileInfo'),
        ),
    ]