# Generated by Django 2.2.7 on 2019-12-01 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20191201_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='text',
            field=models.CharField(max_length=200),
        ),
    ]
