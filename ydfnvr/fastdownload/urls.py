from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('search', views.search, name='search'),
    path('download/<str:data>', views.download, name='download')
]
