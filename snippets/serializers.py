from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User
from rest_framework import permissions


# class SnippetSerializer(serializers.ModelSerializer):
#     owner = serializers.ReadOnlyField(source='owner.username')
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#     class Meta:
#         model = Snippet
#         fields = ['id', 'title', 'code', 'linenos', 'language', 'style', 'owner']



# class UserSerializer(serializers.ModelSerializer):
#     snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#     class Meta:
#         model = User
#         fields = ['id', 'username', 'snippets']



class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Snippet
        fields = ['url', 'id', 'owner', 'title', 'code', 'linenos', 'language', 'style']



class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())
    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'snippets']