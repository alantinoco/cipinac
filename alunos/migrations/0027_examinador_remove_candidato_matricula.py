# Generated by Django 4.0.6 on 2024-02-20 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alunos', '0026_rename_nível_questao_nivel_alter_candidato_matricula'),
    ]

    operations = [
        migrations.CreateModel(
            name='Examinador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('telefone', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.EmailField(blank=True, max_length=50, null=True)),
                ('observacoes', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='candidato',
            name='matricula',
        ),
    ]