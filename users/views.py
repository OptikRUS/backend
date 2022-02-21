from rest_framework.viewsets import ModelViewSet

from users.serializers import UserModelSerializer
from users.models import User


class UserViewSet(ModelViewSet):
    serializer_class = UserModelSerializer
    queryset = User.objects.all()
