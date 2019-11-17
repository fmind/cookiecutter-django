"""Admin panels of the project."""

from django.contrib import admin

from . import models


admin.site.register(models.Snippet)
