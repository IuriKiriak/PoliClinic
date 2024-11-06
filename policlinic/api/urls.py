from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('doctors/', views.DoctorsView.as_view()),
    path('institution/', views.InstitutionView.as_view()),
    path('record/', views.RecordsView.as_view()),
    path('user/', views.UserView.as_view()),
    path('file-pdf/', views.FilePDFView.as_view()),
]

if settings.DEBUG:
    # Добавляем маршрут для медиа-файлов
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)