# Generated by Django 3.0.8 on 2020-08-09 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0015_auto_20200809_1214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devolucao',
            name='data_devolucao',
            field=models.DateTimeField(verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='devolucao',
            name='data_faturada',
            field=models.DateTimeField(verbose_name='date published'),
        ),
    ]