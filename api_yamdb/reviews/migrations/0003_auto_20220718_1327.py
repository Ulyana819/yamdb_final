# Generated by Django 2.2.16 on 2022-07-18 10:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_auto_20220717_2310'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='code_mail',
            new_name='confirmation_code',
        ),
    ]
