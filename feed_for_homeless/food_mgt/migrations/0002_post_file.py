# Generated by Django 3.2.13 on 2022-07-24 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_mgt', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='Files'),
        ),
    ]
