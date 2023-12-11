from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from . models import CustomUser,FriendRequest

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('password', 'email', 'first_name', 'last_name')

class FriendRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = FriendRequest
        fields = '__all__'



# class UserPermissionSerializer(serializers.ModelSerializer):
#     permission = serializers.PrimaryKeyRelatedField(queryset=Permission.objects.all())
#
#     class Meta:
#         model = Userpermissions
#         fields = ['id', 'user_type', 'is_permission','permission']
# class ApartmentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Apartment
#         fields = '__all__'
#
#
class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
class FriendAcceptedlistserializer(serializers.Serializer):
    fiendlist = UserListSerializer(source='requested_to')

class FriendPendinglistserializer(serializers.Serializer):
    fiendlist = UserListSerializer(source='requested_by')




# class AssignedApartmentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = AssignedApartment
#         fields = '__all__'


# class BookSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Booking
#         fields = '__all__'
