# Generated by Django 3.0.8 on 2020-08-09 12:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0014_devolucao'),
    ]

    operations = [
        migrations.RenameField(
            model_name='devolucao',
            old_name='datat_devolucao',
            new_name='data_devolucao',
        ),
    ]
