from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from django.db import connection


from .serializers import UserSerializer
from users.models import CustomUser

class UsersViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()
    permission_classes = [permissions.IsAuthenticated]