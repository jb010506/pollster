# Generated by Django 2.2.7 on 2019-12-01 09:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20191201_1707'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='text',
            new_name='question',
        ),
    ]
