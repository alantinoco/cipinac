# Generated by Django 4.0.6 on 2023-09-30 13:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alunos', '0010_rename_arquivo1_candidato_atestado_acuidade_visual_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='candidato',
            old_name='ctps_contrato_de_trabalhoc',
            new_name='ctps_contrato_de_trabalho',
        ),
        migrations.RenameField(
            model_name='candidato',
            old_name='ctps_identificação',
            new_name='ctps_id',
        ),
        migrations.RenameField(
            model_name='candidato',
            old_name='declaração_participação_exame',
            new_name='declaração_participação',
        ),
        migrations.RenameField(
            model_name='candidato',
            old_name='termos_compromissoia_cpf',
            new_name='termo_compromisso',
        ),
    ]
