from django.contrib.auth import get_user_model
from rest_framework import generics, permissions

from user.serializers import UserSerializer


class UserListAPIView(generics.ListAPIView):
    """
    Returns a list of all users in the database
    """
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)
    queryset = get_user_model().objects.all()  # or override the `get_queryset()` method
