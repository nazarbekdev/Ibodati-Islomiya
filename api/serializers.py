from .models import Mavzu, UsersBot
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer


class CreateDataSerializer(ModelSerializer):
    class Meta:
        model = Mavzu
        fields = ('id', 'qism', 'bolim', 'savol', 'javob')


class CreateDataForSearchSerializer(ModelSerializer):
    qism = serializers.CharField(source='qism.name')
    bolim = serializers.CharField(source='bolim.name')

    class Meta:
        model = Mavzu
        fields = '__all__'


class BotUserSerializer(ModelSerializer):
    class Meta:
        model = UsersBot
        fields = '__all__'
