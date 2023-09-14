# Generated by Django 4.2.5 on 2023-09-13 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='classes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('C_id', models.CharField(max_length=255, unique=True)),
                ('C_name', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ['C_name'],
            },
        ),
    ]
