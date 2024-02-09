# Generated by Django 5.0.1 on 2024-02-05 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('address', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=20)),
            ],
        ),
    ]
