# Generated by Django 3.0.8 on 2020-08-27 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0026_reprogramacao'),
    ]

    operations = [
        migrations.AddField(
            model_name='setor',
            name='idempresa',
            field=models.CharField(default='00000', max_length=10),
        ),
    ]
