from django.contrib import admin
from django.urls import path
from inicio import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('contacto/', views.contacto, name='contacto'),
]