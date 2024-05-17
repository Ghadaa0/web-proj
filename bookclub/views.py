from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from .forms import BookForm


def index(request):
    books = Book.objects.all()
    return render(request, 'bookclub/index.html', {'books': books})


def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookclub/book_list.html', {'books': books})

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'bookclub/add_book.html', {'form': form})

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'bookclub/book_detail.html', {'book': book})

def book_search(request):
    query = request.GET.get('q')
    if query:
        books = Book.objects.filter(title__icontains=query)
    else:
        books = []
    return render(request, 'bookclub/book_search.html', {'books': books})

def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'bookclub/edit_book.html', {'form': form, 'book': book})

def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'bookclub/delete_book.html', {'book': book})