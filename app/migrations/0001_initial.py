# Generated by Django 3.1.4 on 2021-10-09 15:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=255)),
                ('completed', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('priority', models.CharField(choices=[('P1', 'MAJOR'), ('P2', 'NEUTRAL'), ('P3', 'MINOR')], default='P1', max_length=2)),
            ],
        ),
    ]