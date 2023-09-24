from rest_framework import serializers


from api.v1.utile.serializer import CustomAbstractSerializer
from .models import User

class UserSerializer(CustomAbstractSerializer):
    password = serializers.CharField(max_length=255, write_only = True)
    repeat_password = serializers.CharField(max_length=255, write_only = True)
    class Meta:
        model = User
        fields = ("id", "first_name", "last_name", "phone", "email", "role", "address", "direction", "password", "repeat_password")
    
    def validate(self, attrs):
        if not attrs['repeat_password'] and not attrs['repeat_password'] and attrs['repeat_password'] != attrs['repeat_password']:
            raise serializers.ValidationError("Patol to'g'ri kelmadi")
        return attrs
    
    def create(self, validated_data):
        password = validated_data['password']
        validated_data.pop('repeat_password')
        user = User(**validated_data) 
        user.set_password(password)
        user.save()
        return user

class UserUpdateSerializer(CustomAbstractSerializer):
    password = serializers.CharField(max_length=255, write_only = True)
    class Meta:
        model = User
        fields = ("id", "first_name", "last_name", "phone", "email", "role", "address", "direction", "password")
    
    def update(self, instance, validated_data):
        instance.first_name = validated_data.get("first_name", instance.first_name)
        instance.last_name = validated_data.get("last_name", instance.last_name)
        instance.phone = validated_data.get("phone", instance.phone)
        instance.email = validated_data.get("email", instance.email)
        instance.role = validated_data.get("role", instance.role)
        instance.address = validated_data.get("address", instance.address)
        instance.direction = validated_data.get("direction", instance.direction)
        if validated_data.get("password"):
            instance.set_password(validated_data.get("password"))
        instance.save()
        return instance