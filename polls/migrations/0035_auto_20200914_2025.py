# Generated by Django 3.1.1 on 2020-09-14 23:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0034_processo_idcodigo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='processo',
            old_name='idcodigo',
            new_name='idsetor',
        ),
    ]
