from django.shortcuts import render, get_object_or_404
from .models import Book

def HomeView(request):
    return render(request,"index.html")



def ContactView(request):
    return render(request,"contact.html")



def BookListView(request):
    books=Book.objects.all()
    context={
        "books":books
    }
    return render(request,"books-media-gird-view-v2.html",context)



def BookDetailView(request,id):
    book=get_object_or_404(Book,id=id)
    context={
        "book":book
    }
    # return render(request,"detail.html",context)
    return render(request,"books-media-detail-v2.html",context)

