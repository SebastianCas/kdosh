# Generated by Django 2.0.4 on 2019-01-22 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('almacen', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sales',
            name='description',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]
