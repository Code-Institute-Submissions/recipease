# Generated by Django 2.0.7 on 2018-07-24 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0009_auto_20180722_1624'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meal',
            name='user_rating',
        ),
    ]
