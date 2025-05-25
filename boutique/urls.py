from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('bague/<int:pk>/', views.bague_detail, name='bague_detail'),
]
