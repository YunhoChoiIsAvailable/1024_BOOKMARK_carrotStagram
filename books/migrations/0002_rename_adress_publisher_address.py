# Generated by Django 4.1.2 on 2022-11-02 00:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='publisher',
            old_name='adress',
            new_name='address',
        ),
    ]
