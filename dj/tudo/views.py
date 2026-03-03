from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import SingupSerializer, SignInSerializer

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

                response = Response(status=status.HTTP_200_OK)

                response.set_cookie(
                    key='access_token',
                    value=access_token,
                    httponly=True,
                    secure=False,
                    samesite='Lax'
                )
                response.set_cookie(
                    key='refresh_token',
                    value=refresh_token,
                    httponly=True,
                    secure=False,
                    samesite='Lax'
                )
                print(refresh_token)
                return response
            else:
                return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({'Error': str(e)})