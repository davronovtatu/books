from django.urls import path
from .views import HomeView,ContactView,BookListView,BookDetailView

urlpatterns=[
    path('',HomeView,name='home'),
    path('aloqa/',ContactView,name='acloqa'),
    path('booklist/',BookListView,name='listb'),
    path('detail/<int:id>/',BookDetailView,name='det'),
]
