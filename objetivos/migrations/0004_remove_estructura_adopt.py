# Generated by Django 3.1.5 on 2021-02-09 14:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('objetivos', '0003_estructura_adopt'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estructura',
            name='adopt',
        ),
    ]
