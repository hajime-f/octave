# Generated by Django 3.2.7 on 2021-09-06 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='content',
            field=models.TextField(max_length=3000, verbose_name='内容'),
        ),
    ]
