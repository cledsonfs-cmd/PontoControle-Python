# Generated by Django 3.0.8 on 2020-08-17 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0024_processo_producaosetor'),
    ]

    operations = [
        migrations.AddField(
            model_name='setor',
            name='abreviacao',
            field=models.CharField(default='--', max_length=4),
            preserve_default=False,
        ),
    ]
