from rest_framework import serializers

from sports.models import SportCampo, SportCenter


class CampoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'field_number', 'sport_type', 'id_center', 'description', 'price')
        model = SportCampo


class SportCenterSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('author', 'name', 'city', 'phone_number')
        model = SportCenter


class UserEditSportCenterCampiSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('field_number', 'sport_type', 'description', 'price')
        model = SportCampo
