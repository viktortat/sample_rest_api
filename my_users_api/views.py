from .models import MyUser
from .serializers import MyUserSerializer

from rest_framework import viewsets
from rest_framework import filters


class MyUserViewSet(viewsets.ModelViewSet):
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('login',)