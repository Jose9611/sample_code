from rest_framework.permissions import BasePermission
from .models import AssignedApartment,Userpermissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

class CustomPermission(BasePermission):

    def check_permission(request, module):
        if module and request.user:
           is_permission= Userpermissions.objects.select_related('permission').filter(user_type=request.user.user_type,permission__codename=module,is_permission=True)
           if is_permission:
               return True
           else:
               return False



