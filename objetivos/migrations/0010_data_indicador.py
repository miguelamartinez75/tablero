# Generated by Django 3.1.5 on 2021-02-12 15:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('objetivos', '0009_auto_20210212_1223'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='indicador',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='objetivos.indicador'),
        ),
    ]
