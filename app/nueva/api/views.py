from rest_framework.viewsets import ModelViewSet
from nueva.models import post
from .serializers import PostSerializer

class PostApiViwSet(ModelViewSet):
    serializer_class = PostSerializer
    queryset = post.objects.all()
