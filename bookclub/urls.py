from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.book_list, name='book_list'),
    path('add/', views.add_book, name='add_book'),
    path('detail/<int:pk>/', views.book_detail, name='book_detail'),
    path('book/search/', views.book_search, name='book_search'),
    path('book/edit/<int:pk>/', views.edit_book, name='edit_book'),
    path('book/delete/<int:pk>/', views.delete_book, name='delete_book'),

]