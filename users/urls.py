from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'users'

urlpatterns = [
    path('', views.index, name='index'),
    path('search', views.search, name='search'),
    path('add', views.add, name='add'),
    path('save', views.save, name='save'),
    path('<int:id>', views.detail, name='detail'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('delete/<int:id>', views.delete, name='delete')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 