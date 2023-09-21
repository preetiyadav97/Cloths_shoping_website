
# import serializer from rest_framework
from rest_framework import serializers
  
# import model from models.py
from Buy.models import Product,Contact,Cart

# import for user
from django.contrib.auth.models import User
# from Buy.models import Login
  
# Create a model serializer 

class ProductSerializer(serializers.ModelSerializer):
    # specify model and fields
    class Meta:
        model = Product
        fields = '__all__'
        
        
        
class ContactSerializer(serializers.ModelSerializer):
    # specify model and fields
    class Meta:
        model = Contact
        fields = '__all__'
        

class CartSerializer(serializers.ModelSerializer):
    # specify model and fields
    class Meta:
        model = Cart
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = '__all__'
    



# class LoginSerializer(serializers.Serializer):
#     username = serializers.CharField()
#     password = serializers.CharField(write_only=True)
