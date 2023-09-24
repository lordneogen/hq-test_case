from rest_framework import serializers
from .models import *

class SER_CRUD_Persons(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id','name','author')
        read_only_fields=('author',)
    
    def validate(self, attrs):
        if not attrs['name']:
            raise serializers.ValidationError("Нет нужных данных")
        else:
            return super().validate(attrs)