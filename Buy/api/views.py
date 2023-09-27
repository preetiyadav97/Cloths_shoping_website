from rest_framework.views import APIView
from rest_framework.response import Response
from Buy.models import  Product,Contact,Cart
from .serializers import ProductSerializer,ContactSerializer,CartSerializer,UserSerializer,LoginSerializer
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.authentication import JWTAuthentication

from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope
from rest_framework.permissions import IsAuthenticated
from rest_framework import  permissions
class Index(APIView):
    Serializer_classes=ProductSerializer
    permission_classes = (AllowAny,)

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
    def post(self, request, *args, **kwargs):
        try:
            data = request.data
            username = data['username']
            password = data['password']
            
            
            user = authenticate(username=username, password=password)
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            
            return Response( {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        
        except Exception as e:
            context = {
                'success': False,
                "status": status.HTTP_500_INTERNAL_SERVER_ERROR,
                'response': str(e)
            }
            
            return Response(context, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


