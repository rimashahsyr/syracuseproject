# Generated by Django 2.0.13 on 2019-12-04 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userPassword', models.CharField(max_length=2)),
            ],
        ),
        migrations.DeleteModel(
            name='UserInfo',
        ),
    ]
