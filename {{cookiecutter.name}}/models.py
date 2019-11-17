"""Data models of the project."""

from django.db import models


class Snippet(models.Model):
    """A user code snippet."""
    code = models.TextField()
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(
        'auth.User', related_name='snippets', on_delete=models.CASCADE)

    class Meta:
        """Meta of the class."""
        ordering = ['created']

    def __str__(self):
        """Convert to a string."""
        return self.title
