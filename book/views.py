from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import BookSerializer,UserSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from .models import Book
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

@api_view(['POST'])
@csrf_exempt
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(username=username, password=password)

    if user:
        refresh = RefreshToken.for_user(user)
        return Response({
            'access': str(refresh.access_token),
            'refresh': str(refresh)
        })
    else:
        return Response({'error': 'Invalid credentials'}, status=400)
@api_view(['POST','GET'])
@csrf_exempt
def register_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BookListAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user = request.user
        print(user)
        if user.user_type in ['admin','staff','customer']:
            books = Book.objects.all()
            serializer = BookSerializer(books, many=True)
            return Response(serializer.data)
        else:
            data = {"message":"You have no permission"}
            return Response(data)


    def post(self, request):
        user = request.user
        serializer = BookSerializer(data=request.data)
        if user.user_type in ['admin', 'staff']:
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            data = {"message": "You have no permission"}
            return Response(data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





