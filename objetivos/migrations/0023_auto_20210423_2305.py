# Generated by Django 3.1.5 on 2021-04-24 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('objetivos', '0022_objetivo_codigo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='objetivo',
            name='codigo',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
