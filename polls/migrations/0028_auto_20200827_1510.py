# Generated by Django 3.0.8 on 2020-08-27 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0027_setor_idempresa'),
    ]

    operations = [
        migrations.AddField(
            model_name='reprogramacao',
            name='idempresa',
            field=models.CharField(default='00000', max_length=10),
        ),
        migrations.AddField(
            model_name='reprogramacao',
            name='produto',
            field=models.CharField(default='', max_length=100),
        ),
    ]
