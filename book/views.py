from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate, login
from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import UserSerializer,UserListSerializer,FriendRequestSerializer,FriendAcceptedlistserializer,FriendPendinglistserializer,UserRegistrationSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from .models import CustomUser,FriendRequest
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
#from .permissions import CustomPermission
from rest_framework.decorators import api_view, permission_classes
from project.custom_paginator import CustomPageNumberPagination
from django.db.models import  Q,Prefetch
from project.constants import MESSAGES
from django.utils import timezone
from django.contrib.auth import authenticate, login
import jwt



@api_view(['POST'])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')

    user = authenticate(email=email, password=password)
    if not user:
        return Response({'error': 'Email or Password is Incorrect'}, status=400)

    else:

        refresh = RefreshToken.for_user(user)
        return Response({
            'message': 'Login successful',
            'access': str(refresh.access_token),
            'refresh': str(refresh)
        })




@api_view(['POST','GET'])
@csrf_exempt
#@permission_classes([IsAuthenticated,])
def register_user(request):
    serializer = UserRegistrationSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserSearchAPIView(APIView):
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPageNumberPagination
    def post(self, request):
        user = request.user
        users_list = CustomUser.objects.exclude(id=user.id)
        if request.data.get('search'):
            if users_list.filter(email__iexact=request.data.get('search')):
                user = users_list.filter(email__iexact=request.data.get('search')).first()
                serializer = UserListSerializer(user)
                return Response(serializer.data)
            users_list= users_list.filter(first_name__icontains=request.data.get('search'))


        paginator = CustomPageNumberPagination()
        result_page = paginator.paginate_queryset(users_list, request)
        serializer = UserListSerializer(result_page, many=True)
        return Response(serializer.data)


class FriendRequestAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        try:
            res = ''

            user = request.user
            r_to = request.data.get('requested_to')
            req_data = {}
            last_minute = timezone.now() - timezone.timedelta(minutes=1)
            count_within_minute = FriendRequest.objects.filter(Q(created_at__gte=last_minute)&Q(requested_by_id=user.id)).count()
            r_user= CustomUser.objects.filter(id=r_to).first()
            if request.data.get('action') == 'request':
                if FriendRequest.objects.filter(Q(requested_by_id=user.id)&Q(requested_to_id=r_to)).exists():
                    return Response({"message":MESSAGES['REQUEST_ALREAADY_EXIST']})


                elif  count_within_minute >= 3:
                    return Response({"message":MESSAGES['REQUEST_EXCEED']})
                else:

                    req_data['requested_to_id']=r_user.id
                    req_data['requested_by_id'] = user.id
                    out =FriendRequest.objects.create(**req_data)
                    data =FriendRequestSerializer(out).data

                    res ={"data":data,"message":MESSAGES['FRIEND_REQUEST_SUCCESS']}
            elif request.data.get('action') == 'response':
                if not FriendRequest.objects.filter(Q(requested_by_id=r_to)&Q(requested_to_id=user.id)& Q(is_rejected=False)& Q(is_accepted=False)).exists():
                    return Response({"message":MESSAGES['REQUEST_NOT_FOUND']})
                else:
                    if request.data.get('is_regected'):
                        req_data['is_regected'] = True

                    elif request.data.get('is_accepted'):
                        req_data['is_accepted'] = True
                    out =FriendRequest.objects.filter(Q(requested_by_id=r_to) & Q(requested_to_id=user.id)).update(**req_data)
                    res = {"data":"","message":MESSAGES['FRIEND_REQUEST_STATUS_CHANGED']}
            return Response(res)

        except Exception as ex:
            response = self.response(status=False, data=[], msg=MESSAGES['FAILED'])
        return response

class AcceptedListAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        try:
            res = ''

            user = request.user
            if request.data.get('action') =='accepted':
                list =FriendRequest.objects.filter(Q(requested_by_id=user.id)&Q(is_accepted=True)).select_related('requested_to')
                res = FriendAcceptedlistserializer(list, many=True).data
            elif  request.data.get('action') =='pending':
                list = FriendRequest.objects.filter(Q(requested_to_id=user.id) & Q(is_accepted=False)).select_related('requested_by')
                res = FriendPendinglistserializer(list, many=True).data



            return Response(res)

        except Exception as ex:
            response = self.response(status=False, data=[], msg=MESSAGES['FAILED'])
        return response
















#