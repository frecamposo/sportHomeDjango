# Generated by Django 4.2.6 on 2024-04-28 17:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articulo',
            old_name='codigo',
            new_name='id',
        ),
    ]
