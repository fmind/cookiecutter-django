"""Web views of the project."""

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from . import models, permissions, serializers


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """A view set that provides read-only actions."""
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class SnippetViewSet(viewsets.ModelViewSet):
    """A view set that provides model CRUD actions."""
    queryset = models.Snippet.objects.all()
    serializer_class = serializers.SnippetSerializer
    permission_classes = [
        IsAuthenticatedOrReadOnly,
        permissions.IsOwnerOrReadOnly,
    ]

    def perform_create(self, serializer):
        """Associate the owner of the object."""
        serializer.save(owner=self.request.user)


def index(_):
    """View the project home page."""
    return HttpResponse("Hello, world!")


def about(request):
    """View the project about page."""
    return render(request, 'about.html',
                  {'ping': 'pong'})
