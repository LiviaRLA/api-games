from rest_framework import permissions, viewsets
from django.contrib.auth.models import User
from .models import Developer, Platform, Game
from .serializers import DeveloperSerializer, PlatformSerializer, GameSerializer, UserSerializer
from .permissions import IsOwnerOrReadOnly

class DeveloperViewSet(viewsets.ModelViewSet):
    queryset = Developer.objects.all()
    serializer_class = DeveloperSerializer

class PlatformViewSet(viewsets.ModelViewSet):
    queryset = Platform.objects.all()
    serializer_class = PlatformSerializer

class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

class UserViewSet(viewsets.ModelViewSet):

    serializer_class = UserSerializer

    def get_queryset(self):

        if self.action == 'list':
            if self.request.user.is_authenticated:
                return User.objects.filter(id=self.request.user.id)
            else:
                return User.objects.none()
                
        return User.objects.all()


    def get_permissions(self):

        if self.action == 'create' and self.request.user.is_authenticated:
            return [permissions.IsAdminUser()]
        
        return [IsOwnerOrReadOnly()]
