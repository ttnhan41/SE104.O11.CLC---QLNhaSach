from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.



def books(request):
    return render(request, 'books/books.html')

def book(request, pk):
    return render(request, 'books/single-book.html')
