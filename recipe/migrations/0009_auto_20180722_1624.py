# Generated by Django 2.0.7 on 2018-07-22 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0008_auto_20180722_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='image',
            field=models.CharField(blank=True, max_length=180, null=True),
        ),
    ]