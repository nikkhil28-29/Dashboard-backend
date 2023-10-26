from rest_framework import serializers
from account.models import MyUser

class MyUserRegistrationSerializer(serializers.ModelSerializer):

    password2=serializers.CharField(style={'input_type':'password'},write_only=True) # so that passw *******

    class Meta:
        model=MyUser
        fields=['email','name','password','password2','tc']  #for serilizer we ahve to send  theseee
        extar_kwargs={
            'password':{'write_only':True}
        }

    def validate(self,attrs):
        password=attrs.get('password')
        password2=attrs.get('password2')
        if password != password2:

            raise serializers.ValidationError('pass1 & pass2 not match')
        return attrs
    
    #as i have craeted custom model , i need a create method
    def create(self,validate_data):
        return MyUser.objects.create_user(**validate_data)

class LoginSerializer(serializers.ModelSerializer):
    email=serializers.EmailField(max_length=255)

    class Meta:
        model=MyUser
        fields=['email','password']  #for serilizer we ahve to send  theseee
        extar_kwargs={
            'password':{'write_only':True}
        }
