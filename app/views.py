from app.serializers import UserSerializer, ItemSerializer
from aiohttp_rest_framework import views


class UserListCreateView(views.ListCreateAPIView):
    serializer_class = UserSerializer


class UserRetrieveUpdateDestroyView(views.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer


class ItemListCreateView(views.ListCreateAPIView):
    serializer_class = ItemSerializer


class ItemRetrieveUpdateDestroyView(views.RetrieveUpdateDestroyAPIView):
    serializer_class = ItemSerializer
