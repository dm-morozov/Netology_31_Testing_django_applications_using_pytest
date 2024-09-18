from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from app_django_pytest.models import Message
from app_django_pytest.serializers import MessageSerializer


class MessageViewSet(ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer