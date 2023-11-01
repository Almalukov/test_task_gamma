from rest_framework import serializers
from .models import Letter, Parcel

class LetterSerializer(serializers.ModelSerializer):
    """Сериализатор письма"""
    class Meta:
        model = Letter
        fields = '__all__'

class ParcelSerializer(serializers.ModelSerializer):
    """Сериализатор посылки"""
    class Meta:
        model = Parcel
        fields = '__all__'
