# Generated by Django 2.0.1 on 2018-01-09 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_auto_20180108_2214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
