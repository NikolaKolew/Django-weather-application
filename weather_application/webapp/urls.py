from django.urls import path

from weather_application.webapp.views import index, delete_city

urlpatterns = (
    path('', index, name='index'),
    path('delete/<int:pk>', delete_city, name='delete city'),
)
