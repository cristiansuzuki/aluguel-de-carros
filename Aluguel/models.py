from django.db import models

# Create your models here.
class Carros(models.Model):
    carro = models.CharField(max_length=100)
    placa = models.CharField(max_length=10)
    cor = models.CharField(max_length=15)
    chassi = models.CharField(max_length=100)
    published_date = models.DateTimeField(blank=True, null=True, auto_now_add=True)

    class Meta:
        verbose_name = "Carro"
        verbose_name_plural = "Carros"

    def __str__(self):
        return self.carro

class Clientes(models.Model):
    nome_cliente = models.CharField(max_length=200)
    cpf = models.CharField(max_length=20)
    contato = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    published_date = models.DateTimeField(blank=True, null=True, auto_now_add=True)

    def mascara_cpf(self):
        return '%s.%s.%s-%s'%(self.cpf[:3], self.cpf[3:6], self.cpf[6:9], self.cpf[9:11])

    def __str__(self):
        return self.nome_cliente

class Aluguel(models.Model):
    carro = models.ForeignKey(Carros, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    published_date = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    data_saida = models.DateTimeField(blank=True, null=True)
    data_retorno = models.DateTimeField(blank=True, null=True)
    valor = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.cliente.nome_cliente
