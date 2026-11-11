from rest_framework import status
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from .models import User
from rest_framework_simplejwt.tokens import RefreshToken

@api_view(['POST'])
@permission_classes([AllowAny])
def register_view(request):
    email = request.data.get('email')
    password = request.data.get('password')
    if not email:
        return Response({'errors': 'Email must be set'}, status=status.HTTP_400_BAD_REQUEST)
    if User.objects.filter(email=email).exists():
        return Response({'errors': 'Username already exists!'}, status=status.HTTP_400_BAD_REQUEST)
    user = User.objects.create(email=email, password=password)
    refresh = RefreshToken.for_user(user)
    return Response({'refresh': str(refresh),'access': str(refresh.access_token),}, status=status.HTTP_201_CREATED)


api_view(['POST'])
@permission_classes(IsAuthenticated)
def logout_view(request):
    refresh = request.data.get(refresh)

    try:
        token=RefreshToken(refresh)
        token.blacklist
    except:
        return Response({'error':'Token invalid'},status=status.HTTP_400_BAD_REQUEST)

