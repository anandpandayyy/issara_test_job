# Generated by Django 3.2.15 on 2022-09-12 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_pair_store'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='key',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
