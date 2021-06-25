from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'users'

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.add, name='add'),
    path('save', views.save, name='save')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 