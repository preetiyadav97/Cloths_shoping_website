from rest_framework.views import APIView
from rest_framework.response import Response
from Buy.models import  Product,Contact,Cart
from .serializers import ProductSerializer,ContactSerializer,CartSerializer,UserSerializer
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate,login,logout



class Index(APIView):
    def get(self,request,*args, **kwargs):
        try:
            man_products=Product.objects.filter(cat__name="Men")
            woman_products=Product.objects.filter(cat__name="women's")
            kid_products=Product.objects.filter(cat__name="Kids")
            man_pser= ProductSerializer(man_products,many=True)
            woman_pser= ProductSerializer(woman_products,many=True)
            kid_pser= ProductSerializer(kid_products,many=True)
            
            context = {
                'success':True,
                "status":status.HTTP_200_OK,
                'mandata':man_pser.data,
                "womendata":woman_pser.data,
                "kid":kid_pser.data,
            }
            
            return Response(context,status=status.HTTP_200_OK)
        except Exception as e :
            context =  {
                'success':False,
                "status":status.HTTP_400_BAD_REQUEST,
                'response':str(e)
            }
            return Response(context,status=status.HTTP_400_BAD_REQUEST)
        
        
    def post(self, request):
        
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class UserDetailAPI(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, format=None):
        usernames = [user.username for user in User.objects.all()]
        return Response(usernames)
    


class LoginView(APIView):
    def post(self, request,*args, **kwargs):
        try:
            data = request.data

            username = data["username"]
            print(username)
            
            password =data['password']
            print(password)
            print("==============================================")
            user = authenticate(username=username, password=password)
            print(user)
            print("==============================================")
            
            if user is not None:
                context =  {
                'success':True,
                "status":status.HTTP_200_OK,
                'response':f"successfully login {user}"
                }
            
                return Response(context)

            

        except Exception as e:
            context =  {
                'success':False,
                "status":status.HTTP_400_BAD_REQUEST,
                'response':str(e)
                }
            
            return Response(context)
    
