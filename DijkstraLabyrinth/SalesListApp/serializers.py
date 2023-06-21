from rest_framework import serializers
from SalesListApp.models import HepsiBurada


class HepsiBuradaSerializer(serializers.ModelSerializer):
    class Meta:
        model = HepsiBurada
        fields = {
            'id',
            'link',
            'marka'
            'model_adi',
            'prices',
            'puani',
            'ekran_boyutu',
            'islemci',
            'islemci_tipi',
            'isletim_sistemi',
            'ssd_kapasitesi',
            'ram',
        },
