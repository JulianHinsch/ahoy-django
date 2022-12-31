# Generated by Django 4.1.4 on 2022-12-31 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ListenItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=300)),
                ('src', models.CharField(max_length=500)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('start_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='WatchItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
                ('src', models.CharField(max_length=500)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('start_time', models.DateTimeField()),
            ],
        ),
    ]
