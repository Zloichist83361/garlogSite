from rest_framework import serializers 

from calculator.models import Calculate, Term


class CalculateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Calculate
        fields = ('id',
                  'cityto',
                  'cityfrom',
                  'weightto',
                  'weightfrom',
                  'inter_terminal',
                  'pickup',
                  'cargo_delivery',
                  'premium')


class TermSerializer(serializers.ModelSerializer):

    class Meta:
        model = Term
        fields = ('id',
                  'cityto',
                  'cityfrom',
                  'term_standart_to',
                  'term_standart_from',
                  'term_express_to',
                  'term_express_from')

                  