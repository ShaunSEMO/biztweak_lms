from django.conf.urls import url
from . import views
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

app_name = 'lms'

urlpatterns = [
    path('', views.home, name='homepage'),
    path('course/<int:id>', views.view_course, name='viewcourse'),
    path('course/enroll/<int:id>', views.enroll_course, name='enrollcourse'),
    path('course/enroll/module_start/<int:id>', views.start_module, name='startmodule'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)