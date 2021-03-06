# Generated by Django 2.0.4 on 2019-01-11 19:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expenses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=50)),
                ('value', models.IntegerField()),
                ('date', models.DateField(default=datetime.date.today, verbose_name='date')),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod', models.CharField(max_length=4)),
                ('description', models.CharField(max_length=50)),
                ('amoutn', models.IntegerField()),
                ('unitv', models.IntegerField()),
                ('total', models.IntegerField()),
                ('date', models.DateField(default=datetime.date.today, verbose_name='date')),
            ],
        ),
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date.today, verbose_name='date')),
                ('cod', models.CharField(max_length=4)),
                ('unitv', models.IntegerField()),
            ],
        ),
    ]
