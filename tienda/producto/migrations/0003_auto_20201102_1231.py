# Generated by Django 3.1.2 on 2020-11-02 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0002_auto_20201101_2248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='almohada',
            name='material',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='daikimakura',
            name='genero',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='peluche',
            name='tamaño',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
