from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated 

from .serializers import SingupSerializer, SignInSerializer, ListCreateSerializer

# Create your views here.
# Create your views here.
class singup(APIView):
    def post(self, request):
        try:
            serial = SingupSerializer(data=request.data)
            if serial.is_valid():
                serial.save()
                return Response(status=status.HTTP_201_CREATED)
            else:
                return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(str(e))
# Create your views here.
class signin(APIView):
    def post(self, request):
        try:
            serial = SignInSerializer(data=request.data)
            if serial.is_valid():

                refresh_token = serial.validated_data['refresh']
                access_token = serial.validated_data['access']
                userName = serial.validated_data['user']

                response = Response(data={'name': userName},status=status.HTTP_200_OK)

                response.set_cookie(
                    key='access_token',
                    value=access_token,
                    httponly=True,
                    secure=False,
                    samesite='Lax',
                )
                response.set_cookie(
                    key='refresh_token',
                    value=refresh_token,
                    httponly=True,
                    secure=False,
                    samesite='Lax',
                )
                
                return response
            else:
                return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({'Error': str(e)})

# Create your views here.

class listCreate(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        
        try:
            serial = ListCreateSerializer(data=request.data, context={'request':request})
            if serial.is_valid():
                serial.save()
                return Response(status=status.HTTP_201_CREATED)
            else:
                return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(str(e))