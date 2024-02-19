# Generated by Django 4.0.6 on 2023-09-05 21:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('alunos', '0005_empresa_email_empresa_telefone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria_questao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Questao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enunciado', models.TextField()),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='imagens_questoes/')),
                ('A', models.CharField(max_length=100)),
                ('C', models.CharField(max_length=100)),
                ('D', models.CharField(max_length=100)),
                ('E', models.CharField(max_length=100)),
                ('categoria', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='alunos.categoria_questao')),
            ],
        ),
    ]