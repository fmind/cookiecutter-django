"""Model serializers of the project."""

from django.contrib.auth.models import User

from rest_framework import serializers

from . import models


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer of user objects."""
    snippets = serializers.HyperlinkedRelatedField(
        many=True, view_name='snippet-detail', read_only=True)

    class Meta:
        """Meta of the class."""
        model = User
        fields = ['url', 'id', 'username', 'snippets']


class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer of snippet object."""
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        """Meta of the class."""
        model = models.Snippet
        fields = ['id', 'url', 'code', 'title', 'owner']
