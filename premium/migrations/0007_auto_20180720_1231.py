# Generated by Django 2.0.7 on 2018-07-20 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('premium', '0006_premiumuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='premium',
            name='user_id',
            field=models.IntegerField(unique=True),
        ),
    ]
