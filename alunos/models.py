from django.db import models
import uuid

class Empresa(models.Model):
    razao_social = models.CharField(max_length=100)
    nome_fantasia = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=14, unique=True)
    email = models.EmailField(max_length=50, null=True, blank=True, unique=True)
    telefone = models.CharField(max_length=11, null=True, blank=True)
    representante_legal = models.CharField(max_length=100)
    cpf_representante_legal = models.CharField(max_length=11)

    def __str__(self):
        return self.razao_social



class Examinador(models.Model):
    nome = models.CharField(max_length=50)
    telefone = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=50, null=True, blank=True)
    observacoes = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nome


class Exame(models.Model):

    HORA =  (
        ('08:00', '08:00'),
        ('09:00', '09:00'),
        ('10:00', '10:00'),
        ('11:00', '11:00'),
        ('12:00', '12:00'),
        ('13:00', '13:00'),
        ('14:00', '14:00'),
        ('15:00', '15:00'),
        ('16:00', '16:00'),
        ('17:00', '17:00'),
        ('18:00', '18:00'),
        ('19:00', '19:00'),
        ('20:00', '20:00'),

    )

    nome_da_turma = models.CharField(max_length=50)
    titulo_do_certificado = models.CharField(max_length=100)
    empresa = models.ForeignKey(Empresa, null=True, blank=True, on_delete=models.SET_NULL)
    examinador = models.ForeignKey(Examinador, null=True, blank=True, on_delete=models.SET_NULL)
    data_da_prova = models.DateField(null=False, blank=False)
    hora = models.CharField(max_length=10, choices=HORA)

    def __str__(self):
        return self.nome_da_turma



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
    orgao_emissor = models.CharField(max_length=15, null=True, blank=True)
    data_emissao = models.DateField(null=True, blank=True)
    empresa = models.ForeignKey(Empresa, null=True, blank=True, on_delete=models.SET_NULL)
    turma = models.ForeignKey(Exame, null=True, blank=True, on_delete=models.SET_NULL)

    # Endereço
    logradouro = models.CharField(max_length=100)
    numero_casa = models.CharField(max_length=10)
    complemento = models.CharField(max_length=30, null=True, blank=True)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=50, choices=ESTADOS)

    # Contatos
    telefone = models.CharField(max_length=11)
    telefone2 = models.CharField(max_length=11, null=True, blank=True)
    email = models.EmailField(max_length=50, null=True, blank=True, unique=True)

    # Documentos adicionais
    atestado_acuidade_visual = models.FileField(upload_to ='arquivos/', null=True, blank=True)
    ctps_id = models.FileField(upload_to ='arquivos/', null=True, blank=True)
    ctps_contrato_de_trabalho = models.FileField(upload_to ='arquivos/', null=True, blank=True)
    comprovante_escolaridade = models.FileField(upload_to ='arquivos/', null=True, blank=True)
    comprovante_residencia = models.FileField(upload_to ='arquivos/', null=True, blank=True)
    copia_identidade = models.FileField(upload_to ='arquivos/', null=True, blank=True)
    copia_cpf = models.FileField(upload_to ='arquivos/', null=True, blank=True)
    termo_compromisso = models.FileField(upload_to ='arquivos/', null=True, blank=True)
    codigo_conduta = models.FileField(upload_to ='arquivos/', null=True, blank=True)
    declaracao_participacao = models.FileField(upload_to ='arquivos/', null=True, blank=True)
    instrucao_candidato = models.FileField(upload_to ='arquivos/', null=True, blank=True)
    registro_solicitacao_exame = models.FileField(upload_to ='arquivos/', null=True, blank=True)

    def __str__(self):
        return f"{self.nome} - {self.cpf}"


class Categoria_questao(models.Model):
    nome = models.CharField(max_length=100)
    def __str__(self):
        return self.nome

class Questao(models.Model):

    NIVEL =  (
        ("Fácil", "Fácil"),
        ("Difícil", "Difícil"),
    )

    CORRETA =  (
        ("A", "A"),
        ("B", "B"),
        ("C", "C"),
        ("D", "D"),
    )

    enunciado = models.TextField()
    imagem = models.ImageField(null=True, blank=True, upload_to='imagens_questoes/')
    categoria = models.ForeignKey(Categoria_questao, null=True, blank=True, on_delete=models.SET_NULL)
    nivel = models.CharField(max_length=50, choices=NIVEL)
    a = models.CharField(max_length=100)
    b = models.CharField(max_length=100)
    c = models.CharField(max_length=100)
    d = models.CharField(max_length=100)
    resposta_correta = models.CharField(max_length=50, choices=CORRETA)

    def __str__(self):
        return self.enunciado


class Solicitacao(models.Model):

    TIPO =  (
        ("Geral", "Geral"),
        ("Apelação", "Apelação"),
        ("Reclamação", "Reclamação")
    )

    tipo = models.CharField(max_length=20, choices=TIPO)
    protocolo = models.CharField(max_length=100, null=True, blank=True)
    titulo = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    telefone = models.CharField(max_length=11)
    texto = models.TextField()
    anotacoes_cipinac = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.titulo


class Certificado(models.Model):
    identificador = models.UUIDField(primary_key = False, default = uuid.uuid4, editable = False)
    nome = models.CharField(max_length=100)
    CPF = models.CharField(max_length=11)
    titulo_do_certificado = models.CharField(max_length=100)
    data = models.DateField(null=False, blank=False)
    validade = models.DateField(null=False, blank=False)
    certificado = models.FileField(upload_to ='certificados/', null=True, blank=True)

    def __str__(self):
        return f"{self.nome} - {self.titulo_do_certificado} - ID: "+ str(self.identificador)




