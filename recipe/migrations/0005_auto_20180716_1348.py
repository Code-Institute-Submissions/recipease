# Generated by Django 2.0.7 on 2018-07-16 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0004_auto_20180716_1346'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='meal',
        ),
        migrations.AddField(
            model_name='meal',
            name='comment',
            field=models.ManyToManyField(to='recipe.Comment'),
        ),
    ]
