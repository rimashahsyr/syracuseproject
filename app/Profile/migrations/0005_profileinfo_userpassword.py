# Generated by Django 2.0.13 on 2019-12-04 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0004_auto_20191201_0644'),
    ]

    operations = [
        migrations.AddField(
            model_name='profileinfo',
            name='userPassword',
            field=models.CharField(default='pass', max_length=250),
            preserve_default=False,
        ),
    ]
