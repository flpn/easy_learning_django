# Generated by Django 2.0.1 on 2018-01-11 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0006_auto_20180110_2253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='text',
            field=models.TextField(max_length=500),
        ),
    ]