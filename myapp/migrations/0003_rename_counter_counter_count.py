# Generated by Django 5.1.6 on 2025-02-26 06:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_rename_mymodel_counter'),
    ]

    operations = [
        migrations.RenameField(
            model_name='counter',
            old_name='counter',
            new_name='count',
        ),
    ]
