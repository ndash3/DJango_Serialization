from rest_framework import serializers
from .models import PassengerClass

class PassengerSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=40)
    city = serializers.CharField(max_length=30)
    rewards = serializers.IntegerField()

    def create(self, validated_data):
        return PassengerClass.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.city = validated_data.get('city', instance.city)
        instance.rewards = validated_data.get('rewards', instance.rewards)
        instance.save()
        return instance