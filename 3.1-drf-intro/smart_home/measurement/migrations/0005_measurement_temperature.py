# Generated by Django 4.1.1 on 2022-09-28 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0004_remove_measurement_temperature_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='measurement',
            name='temperature',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
