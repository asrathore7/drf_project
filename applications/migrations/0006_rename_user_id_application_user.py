# Generated by Django 3.2.9 on 2021-12-10 09:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0005_application_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='application',
            old_name='user_id',
            new_name='user',
        ),
    ]
