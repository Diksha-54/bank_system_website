# Generated by Django 3.0.8 on 2021-02-13 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20210213_1830'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction_deatials',
            name='Receiver_updated_Balance',
            field=models.IntegerField(default=0),
        ),
    ]
