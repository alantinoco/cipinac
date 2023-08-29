from django.db import models

class Empresa(models.Model):
    razao_social = models.CharField(max_length=100)
    nome_fantasia = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=14, unique=True)
    representante_legal = models.CharField(max_length=100)
    cpf_representante_legal = models.CharField(max_length=11)

    def __str__(self):
        return self.razao_social


class Candidato(models.Model):

    NACIONALIDADE =  (
        ("BR", "Brasileira"),
        ("EST", "Estrangeira"),
    )

    SEXO =  (
        ("M", "Masculino"),
        ("F", "Feminino"),
    )

    ESTADOS =  (
        ('AC', 'Acre'),
        ('AL',	'Alagoas'),
        ('AP',	'Amapá'),
        ('AM',	'Amazonas'),
        ('BA',	'Bahia'),
        ('CE',	'Ceara'),
        ('DF',	'Distrito Federal'),
        ('ES',	'Espírito Santo'),
        ('GO',	'Goiás'),
        ('MA',	'Maranhão'),
        ('MT',	'Mato Grosso'),
        ('MS',	'Mato Grosso do Sul'),
        ('MG',	'Minas Gerais'),
        ('PA',	'Pará'),
        ('PB',	'Paraíba'),
        ('PR',	'Paraná'),
        ('PE',	'Pernambuco'),
        ('PI',	'Piauí'),
        ('RJ',	'Rio de Janeiro'),
        ('RN',	'Rio Grande do Norte'),
        ('RS',	'Rio Grande do Sul'),
        ('RO',	'Rondônia'),
        ('RR',	'Roraima'),
        ('SC',	'Santa Catarina'),
        ('SP',	'São Paulo'),
        ('SE',	'Sergipe'),
        ('TO',	'Tocantins'),
    )


    # Dados pessoais
    foto = models.ImageField(null=True, blank=True, upload_to='fotos/')
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True)
    sexo = models.CharField(max_length=10, choices=SEXO)
    data_nasc = models.DateField(null=True, blank=True)
    nacionalidade = models.CharField(max_length=50, choices=NACIONALIDADE)
    identidade = models.CharField(max_length=11, unique=True, null=True, blank=True)
    orgao_emissor = models.CharField(max_length=15, unique=True, null=True, blank=True)
    data_emissao = models.DateField(null=True, blank=True)
    empresa = models.ForeignKey(Empresa, null=True, blank=True, on_delete=models.SET_NULL)

    # Endereço
    logradouro = models.CharField(max_length=100)
    numero_casa = models.CharField(max_length=10)
    complemento = models.CharField(max_length=15, null=True, blank=True)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=50, choices=ESTADOS)

    # Contatos
    telefone = models.CharField(max_length=11)
    telefone2 = models.CharField(max_length=11, null=True, blank=True)
    email = models.EmailField(max_length=50, null=True, blank=True, unique=True)

    def __str__(self):
        return f"{self.nome} - {self.cpf}"
