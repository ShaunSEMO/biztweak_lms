from django.conf.urls import url
from . import views
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

app_name = 'lms'

urlpatterns = [
    path('home', views.home, name='homepage'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)