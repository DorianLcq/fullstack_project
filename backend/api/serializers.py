from django.contrib.auth.models import User
from rest_framework import serializers 

class UserSerializer(serializers.HyperlinkedModelSerializer) : 
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password' : {'write_only' : True, 'required' : True} }

    def create(self, validated_area) :
         user = User.objects.create_user(**validated_area)
         return user

         