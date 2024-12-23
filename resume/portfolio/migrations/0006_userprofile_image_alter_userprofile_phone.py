# Generated by Django 5.1.1 on 2024-10-29 09:47

import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='upload_media/'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region='RU'),
        ),
    ]
