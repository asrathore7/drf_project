# Generated by Django 3.2.9 on 2021-12-08 10:16

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_user_phonenumber'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='country',
            field=django_countries.fields.CountryField(blank=True, max_length=30),
        ),
    ]
