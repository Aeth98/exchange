# Generated by Django 3.2.5 on 2021-07-20 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='profit_loss',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='usd_balance',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
