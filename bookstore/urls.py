from django.urls import path
from . import views

urlpatterns = [
    path('', views.bookstore, name="bookstore"),
    path('book/<str:pk>/', views.book, name="book"),
    path('import-book/', views.importBook, name="import-book"),
    path('create-receipt/', views.createReceipt, name="create-receipt"),
    path('search-books/', views.searchBooks, name="search-books"),
    path('search-guests/', views.searchGuests, name="search-guests"),
]