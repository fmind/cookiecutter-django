"""Application routes of the project."""

from django.contrib import admin
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static

from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls

from . import views


API_TITLE = 'Web API'
API_DESCRIPTION = 'Web API Description'

router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'snippets', views.SnippetViewSet)

urlpatterns = [
    url(r'^api/docs/', include_docs_urls(title=API_TITLE, description=API_DESCRIPTION)),
    url(r'^api/auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/schema/', get_schema_view(title=API_TITLE)),
    url(r'^api/v1/', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^about.html$', views.about, name='about'),
    url(r'^$', views.index, name='index'),
] + static(settings.STATIC_URL)
