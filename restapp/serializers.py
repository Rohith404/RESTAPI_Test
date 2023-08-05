from rest_framework import serializers
from .models import Article, Magazine, Author

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class MagazineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Magazine
        fields = '__all__'

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'

class ArticleDetailSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    magazines = MagazineSerializer(many=True)

    class Meta:
        model = Article
        fields = '__all__'

    