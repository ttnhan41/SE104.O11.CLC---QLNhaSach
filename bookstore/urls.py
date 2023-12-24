from django.urls import path
from . import views

urlpatterns = [
    path('', views.bookstore, name="book-store"),
    path('book/<str:pk>/', views.book, name="book"),
    path('import-book/', views.importBook, name="import-book"),
    path('search-import-notes/', views.searchImportNotes, name="search-import-notes"),
    path('create-receipt/', views.createReceipt, name="create-receipt"),
    path('search-books/', views.searchBooks, name="search-books"),
    path('search-authors/', views.searchAuthors, name="search-authors"),
    path('search-categories/', views.searchCategories, name="search-categories"),
    path('search-guests/', views.searchGuests, name="search-guests"),
    path('create-books-bill/', views.createBooksBill, name="create-books-bill"),
    path('search-bills/', views.searchBills, name="search-bills"),
    path('input-payment/', views.inputPayment, name="input-payment"),
    path('create-inventory-report/', views.createInventoryReport, name="create-inventory-report"),
    path('search-inventory-report/', views.searchInventoryReport, name="search-inventory-report"),
    path('create-debt-report/', views.createDebtReport, name="create-debt-report"),
    path('search-debt-report/', views.searchDebtReport, name="search-debt-report"),
    path('change-rules/', views.changeRules, name="change-rules"),
    path('bill/', views.exportBill, name="bill"),
    path('import-note/', views.exportImportingNote, name="import-note"),
    path('inventory-report/', views.exportInventoryReport, name="inventory-report"),
    path('debt-report/', views.exportDebtReport, name="debt-report"),
]