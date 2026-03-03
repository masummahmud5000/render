from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import SingupSerializer

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