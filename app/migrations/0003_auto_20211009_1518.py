# Generated by Django 3.1.4 on 2021-10-09 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20211009_1514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='id',
            field=models.UUIDField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]