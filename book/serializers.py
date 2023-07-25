from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from . models import Booking,Apartment,Flat,AssignedApartment,Userpermissions

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name','user_type')

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password:
            instance.set_password(password)
        instance.save()
        return instance


class UserPermissionSerializer(serializers.ModelSerializer):
    permission = serializers.PrimaryKeyRelatedField(queryset=Permission.objects.all())

    class Meta:
        model = Userpermissions
        fields = ['id', 'user_type', 'is_permission','permission']
class ApartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apartment
        fields = '__all__'


class FlatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flat
        fields = '__all__'

class AssignedApartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssignedApartment
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
