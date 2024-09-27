from rest_framework import serializers
from rest_framework.serializers import  ModelSerializer,Serializer
from  .models import profile



class profile_serializer(serializers.ModelSerializer):
    class Meta:
         model=profile
         fields=["first_name","second_name","email","mobile"]

    def validate_first_name(self,value):
        if 'mani' in value:
            raise  serializers.ValidationError("mani is not allowed to create account")
        return value