from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from .serializers import RegisterSerializers, UserSerializers
from rest_framework.exceptions import AuthenticationFailed
from .filters import UsersFilterBackend
from datetime import datetime, timedelta
from rest_framework.views import APIView


class RegisterAPIView(generics.GenericAPIView):
    serializer_class = RegisterSerializers

    def post(self, request):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({
                "Message": "User created successfully",
                "User": serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response({"errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class UserListAPIView(ListAPIView):
    serializer_class = UserSerializers
    queryset = User.objects.all()
    filter_backends = (UsersFilterBackend,)