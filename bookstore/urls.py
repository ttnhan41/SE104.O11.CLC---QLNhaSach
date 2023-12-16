from django.urls import path
from . import views

urlpatterns = [
    path('', views.bookstore, name="bookstore"),
    path('book/<str:pk>/', views.book, name="book"),
    path('import-book/', views.importBook, name="import-book"),
    path('create-receipt/', views.createReceipt, name="create-receipt"),
    path('search-books/', views.searchBooks, name="search-books"),
    path('search-guests/', views.searchGuests, name="search-guests"),
    path('create-books-bill/', views.createBooksBill, name="create-books-bill"),
    path('search-bills/', views.searchBills, name="search-bills"),
    path('input-payment/', views.inputPayment, name="input-payment"),
    path('create-inventory-report/', views.createInventoryReport, name="create-inventory-report"),
    path('search-inventory-report/', views.searchInventoryReport, name="search-inventory-report"),

    path('change-rules/', views.changeRules, name="change-rules"),
]