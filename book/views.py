from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import BookSerializer,UserSerializer,ApartmentSerializer,FlatSerializer,AssignedApartmentSerializer,UserPermissionSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from .models import Booking,CustomUser
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .permissions import CustomPermission
from rest_framework.decorators import api_view, permission_classes



class UserPermissionAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):

        if CustomPermission.check_permission(request,'add_permission'):
            user = request.user
            serializer = UserPermissionSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'message': 'You have no permission'})


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
#@permission_classes([IsAuthenticated,])
def register_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BookListAPIView(APIView):
    permission_classes = [CustomPermission,IsAuthenticated]
    def get(self, request):
        user = request.user
        books = Booking.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
        return Response(data)


    def post(self, request):
        user = request.user
        request.data['user_id'] = user.id

        request.data['total'] = request.data['price']+request.data['gst_amount']
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ApartmentAPIView(APIView):
    permission_classes = [CustomPermission,IsAuthenticated]

    def post(self, request):
        user = request.user
        serializer = ApartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FlatAPIView(APIView):
    permission_classes = [CustomPermission,IsAuthenticated]

    def post(self, request):
        user = request.user
        serializer = FlatSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AssignApartmentAPIView(APIView):
    permission_classes = [CustomPermission,IsAuthenticated]

    def post(self, request):
        user = request.user
        serializer = AssignedApartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
