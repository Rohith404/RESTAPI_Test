from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Magazine,Author,Article
from .serializers import MagazineSerializer, ArticleSerializer,AuthorSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    @action(detail=True, methods=['GET'])
    def articles(self, request, pk=None):
        try:
            author = self.get_object()
            articles = Article.objects.filter(author=author)
            serializer = ArticleSerializer(articles, many=True)
            return Response(serializer.data)
        except Article.DoesNotExist:
            return Response({"error": "Author not found"}, status=status.HTTP_404_NOT_FOUND)


class MagazineViewSet(viewsets.ModelViewSet):
    queryset = Magazine.objects.all()
    serializer_class = MagazineSerializer

    @action(detail=True, methods=['get'])
    def articles(self, request, pk=None):
        magazine = self.get_object()
        articles = magazine.article_set.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

