from rest_framework import serializers
from .models import User, Employer
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken


class User_Seri(serializers.ModelSerializer):
    class Meta:
        model=User
        fields= ['id','first_name','last_name','email']

    
class Sign_Up_Seri(serializers.ModelSerializer):
    password= serializers.CharField(write_only= True)
    class Meta:
        model=  User
        fields= ['first_name', 'last_name','email','password']    
    def create(self, data):
        if not data:
            raise serializers.ValidationError("Missing field!")
        return User.objects.create_user(**data)


    
class Login_Seri(serializers.Serializer):
    email= serializers.EmailField()
    password = serializers.CharField(write_only= True)   

    def validate( self,attrs):
        user= authenticate(email=attrs['email'], password= attrs['password'])
        if not user:
            raise serializers.ValidationError("Invalid Form's Field!")
        ref= RefreshToken.for_user(user)
        return { 'refresh': str(ref),
            'access': str(ref.access_token)} 


class Employer_Seri( serializers.ModelSerializer):
    class Meta:
        model= Employer
        fields= '__all__'