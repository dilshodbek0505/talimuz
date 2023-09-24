from rest_framework import serializers


from api.v1.utile.serializer import CustomAbstractSerializer
from .models import (
    School, 
    SchoolImage
)
class SchoolImageSerializer(CustomAbstractSerializer):
    class Meta:
        model = SchoolImage
        fields = ("id", "school", "image")
    

class SchoolSerializer(CustomAbstractSerializer):
    images = SchoolImageSerializer(many = True)
    class Meta:
        model = School
        fields = ("id", "name", "address", "user", "direction", "images")
    
    def to_representation(self, instance):
        res = super().to_representation(instance)
        res['user'] = {
            "first_name": instance.user.first_name,
            "last_name": instance.user.last_name,
            "phone": instance.user.phone
        }
        return res

