# Generated by Django 3.1.5 on 2021-02-12 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('objetivos', '0006_auto_20210212_1214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parametro',
            name='parama',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='parametro',
            name='paramb',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='parametro',
            name='paramc',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='parametro',
            name='paramd',
            field=models.FloatField(blank=True, null=True),
        ),
    ]