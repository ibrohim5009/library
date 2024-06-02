# Generated by Django 5.0.6 on 2024-06-02 08:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.TextField(auto_created=250)),
                ('name', models.TextField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Last_name', models.TextField()),
                ('First_name', models.TextField()),
                ('location', models.TextField()),
                ('card_number_Seria', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Kitob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.TextField(auto_created=250)),
                ('image', models.FileField(upload_to='%id_%m_%Y/')),
                ('name', models.TextField(max_length=250)),
                ('amount', models.BigIntegerField()),
                ('rent_price', models.FloatField()),
                ('ISBN', models.UUIDField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.category')),
            ],
        ),
        migrations.CreateModel(
            name='Rent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.BigIntegerField()),
                ('amount', models.BigIntegerField()),
                ('return_time', models.TimeField()),
                ('kitob', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.kitob')),
            ],
        ),
    ]
