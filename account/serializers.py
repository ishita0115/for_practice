from rest_framework import serializers
from account.models import User,House
from xml.dom import ValidationErr
class UserRegisterationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':'password'},write_only=True)
    class Meta:
        model = User
        fields=['email','name','password','password2']
        
        extra_kwargs={
            'password':{'write_only':True}
        }
    def validate(self, attrs):
        password = attrs.get('password')
        print(password)
        password2 = attrs.get('password2')
        if password != password2:
            raise serializers.ValidationError("Password and Confirm Password doesn't match")
        return attrs
    def create(self,validate_data):
        return User.objects.create_user(**validate_data)
    
class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)
    class Meta:
        model = User
        fields=['email','password']

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','email','name']

class ChangePasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=255, style={'input_type': 'password'} ,write_only=True, required=True)
    password2 = serializers.CharField(max_length=255, style={'input_type': 'password'} ,write_only=True, required=True)
    class Meta :
        model = User
        fields = ['password', 'password2']

    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')
        user = self.context.get('user')
        if password != password2:
            raise serializers.ValidationError("Password and Confirm Password doesn't match")
        user.set_password(password)
        user.save()
        return attrs
        
class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = '__all__'