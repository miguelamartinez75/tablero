# Generated by Django 3.1.5 on 2021-04-24 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('objetivos', '0021_objetivo_prefer'),
    ]

    operations = [
        migrations.AddField(
            model_name='objetivo',
            name='codigo',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
