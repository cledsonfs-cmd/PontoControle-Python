# Generated by Django 3.0.8 on 2020-08-10 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0021_auto_20200810_1300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devolucao',
            name='data_devolucao',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='devolucao',
            name='data_faturada',
            field=models.DateField(),
        ),
    ]