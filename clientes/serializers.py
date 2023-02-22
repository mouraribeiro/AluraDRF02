from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import *


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

    def validate(self, data):
        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError({'cpf': "Número CPF inválido."})
        if not nome_valido(data['nome']):
            raise serializers.ValidationError({'Nome': 'Não inclua números nesse campo.'})

        if not rg_valido(data['rg']):
            raise serializers.ValidationError({'RG': 'O RG deve ter 9 dígitos.'})

        if not celular_valido(data['celular']):
            raise serializers.ValidationError({'Celular': 'O número precisa estar no formato: XX XXXXX-XXXX'})

        return data

