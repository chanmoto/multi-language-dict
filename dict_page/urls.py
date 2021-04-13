from django.urls import path,reverse
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('get_query', views.get_query, name='query'),
    path('about/', views.about, name='about'),
    path('search/', views.search, name ='search'),
    path('delete/<id>', views.delete, name='delete'),
    path('content/', views.content, name='content'),
    path('translate/', views.translate, name='translate'),
]
