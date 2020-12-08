# Generated by Django 3.1.3 on 2020-11-24 15:53

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0015_auto_20200730_1041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=autoslug.fields.AutoSlugField(verbose_name=models.SlugField(unique=True)),
        ),
        migrations.AlterField(
            model_name='notebook',
            name='slug',
            field=autoslug.fields.AutoSlugField(verbose_name=models.SlugField(unique=True)),
        ),
        migrations.AlterField(
            model_name='smartphone',
            name='slug',
            field=autoslug.fields.AutoSlugField(verbose_name=models.SlugField(unique=True)),
        ),
    ]