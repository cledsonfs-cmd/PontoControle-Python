# Generated by Django 3.1.1 on 2020-09-18 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0044_ponto_controle_campos'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ponto_Controle_Campos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(default='', max_length=15)),
            ],
        ),
    ]
