# Generated by Django 3.0.8 on 2020-07-27 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_relatorio'),
    ]

    operations = [
        migrations.AddField(
            model_name='empresa',
            name='apelido',
            field=models.CharField(default='empresa', max_length=15),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='empresa',
            name='nome',
            field=models.CharField(default='empresa', max_length=255),
        ),
    ]
