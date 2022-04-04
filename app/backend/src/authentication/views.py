from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action, renderer_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import logout

from core.views import SerializerViewSetMixin
from authentication.serializers import RegisterSerializer, LoginSerializer
from authentication.renderer import UserJSONRenderer


class AuthViewSet(SerializerViewSetMixin, ViewSet):
    permission_classes = (AllowAny, )
    serializers = {
        'register': RegisterSerializer,
        'login': LoginSerializer,
    }

    @action(methods=['POST'], detail=False)
    @renderer_classes((UserJSONRenderer,))
    def register(self, request):
        user = request.data.get('user', {})
        serializer = self.get_serializer_class()
        serializer = serializer(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @renderer_classes((UserJSONRenderer,))
    @action(methods=['POST'], detail=False)
    def login(self, request):
        user = request.data.get('user', {})
        serializer = self.get_serializer_class()
        serializer = serializer(data=user)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    @renderer_classes((UserJSONRenderer,))
    @action(methods=['POST'], detail=False)
    def logout(self, request):
        return logout(request)
