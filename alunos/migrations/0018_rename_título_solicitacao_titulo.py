# Generated by Django 4.0.6 on 2024-01-07 18:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alunos', '0017_rename_solicitação_solicitacao'),
    ]

    operations = [
        migrations.RenameField(
            model_name='solicitacao',
            old_name='título',
            new_name='titulo',
        ),
    ]
