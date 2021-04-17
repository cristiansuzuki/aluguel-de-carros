from django import forms
from .models import *


class CarrosForm(forms.ModelForm):
    class Meta:
        model = Carros
        fields = ('carro', 'placa', 'cor', 'chassi')
        widgets = {
            'carro': forms.TextInput(
                attrs={'type': 'text', 'class': 'form-control form-control-user', 'id': 'exampleInputName',
                       'placeholder': 'Marca e modelo do automóvel'}),
            'placa': forms.TextInput(
                attrs={'type': 'text', 'class': 'form-control form-control-user', 'id': 'exampleInputName',
                       'placeholder': 'Placa'}),
            'cor': forms.TextInput(
                attrs={'type': 'text', 'class': 'form-control form-control-user', 'id': 'exampleInputName',
                       'placeholder': 'Cor'}),
            'chassi': forms.TextInput(
                attrs={'type': 'text', 'class': 'form-control form-control-user', 'id': 'exampleInputName',
                       'placeholder': 'Chassi'}),
        }


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Clientes
        fields = ('nome_cliente', 'cpf', 'contato', 'email')
        widgets = {
            'nome_cliente': forms.TextInput(
                attrs={'type': 'text', 'class': 'form-control form-control-user', 'id': 'exampleInputName',
                       'placeholder': 'Nome completo'}),
            'cpf': forms.TextInput(
                attrs={'type': 'text', 'class': 'form-control form-control-user', 'id': 'exampleInputEmail',
                       'placeholder': 'CPF'}),
            'contato': forms.TextInput(
                attrs={'type': 'text', 'class': 'form-control form-control-user', 'id': 'inputPhone',
                       'placeholder': 'Contato'}),
            'email': forms.TextInput(
                attrs={'type': 'email', 'class': 'form-control form-control-user', 'id': 'exampleInputEmail',
                       'placeholder': 'E-mail'}),
        }


class AluguelForm(forms.ModelForm):
    class Meta:
        model = Aluguel
        fields = ('carro', 'data_saida', 'data_retorno', 'valor')
        widgets = {
            'carro': forms.Select(
                attrs={'type': 'select', 'class': 'form-control', 'id': 'exampleInputSelect',
                       'placeholder': '', 'value': '10'}),
            'data_saida': forms.DateInput(
                attrs={'type': 'date', 'class': 'form-control form-control-user', 'id': 'exampleInputDate',
                       'placeholder': 'Data de Saída do Veículo'}),
            'data_retorno': forms.DateInput(
                attrs={'type': 'date', 'class': 'form-control form-control-user', 'id': 'exampleInputDate',
                       'placeholder': 'Data do Retorno do Veículo'}),
            'valor': forms.TextInput(
                attrs={'type': 'number','step': '0.01', 'class': 'form-control form-control-user', 'id': 'formGroupExampleInput',
                       'placeholder': 'Valor'}),
        }


