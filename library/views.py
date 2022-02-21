from rest_framework.viewsets import ModelViewSet

from library.serializers import AuthorModelSerializer
from library.models import Author


class AuthorViewSet(ModelViewSet):
    serializer_class = AuthorModelSerializer
    queryset = Author.objects.all()
