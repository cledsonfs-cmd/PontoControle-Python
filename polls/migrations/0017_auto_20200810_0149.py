# Generated by Django 3.0.8 on 2020-08-10 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0016_auto_20200809_1255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devolucao',
            name='data_devolucao',
            field=models.DateField(verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='devolucao',
            name='data_faturada',
            field=models.DateField(verbose_name='date published'),
        ),
    ]
