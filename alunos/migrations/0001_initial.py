# Generated by Django 4.0.6 on 2023-07-30 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('cpf', models.CharField(max_length=11, unique=True)),
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino')], max_length=10)),
                ('data_nasc', models.DateField(blank=True, null=True)),
                ('nacionalidade', models.CharField(choices=[('BR', 'Brasileira'), ('EST', 'Estrangeira')], max_length=50)),
                ('identidade', models.CharField(blank=True, max_length=11, null=True, unique=True)),
                ('orgao_emissor', models.CharField(blank=True, max_length=15, null=True, unique=True)),
                ('data_emissao', models.DateField(blank=True, null=True)),
                ('logradouro', models.CharField(max_length=100)),
                ('numero_casa', models.CharField(max_length=10)),
                ('complemento', models.CharField(blank=True, max_length=15, null=True)),
                ('cidade', models.CharField(max_length=100)),
                ('estado', models.CharField(choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceara'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')], max_length=50)),
                ('telefone', models.CharField(max_length=11)),
                ('telefone2', models.CharField(blank=True, max_length=11, null=True)),
                ('email', models.EmailField(blank=True, max_length=50, null=True, unique=True)),
            ],
        ),
    ]
