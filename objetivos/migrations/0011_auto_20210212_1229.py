# Generated by Django 3.1.5 on 2021-02-12 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('objetivos', '0010_data_indicador'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='value',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
