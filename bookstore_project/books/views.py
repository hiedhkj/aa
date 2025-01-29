from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.contrib import messages
from .models import Book
from users.models import UserAccount

# Create your views here.

class BookDetailView(View):
    def get(self, request, id):
        book = get_object_or_404(Book, id=id)
        user_info = None
        if 'user_id' in request.session:
            try:
                user_info = UserAccount.objects.get(id=request.session['user_id'])
            except UserAccount.DoesNotExist:
                user_info = None
        same_genre_books = Book.objects.filter(genre=book.genre).exclude(id=book.id)[:10]
        return render(request, 'book.html', {'book': book, 'user': user_info, 'same_genre_books': same_genre_books})

class BuyNowView(View):
    def get(self, request, id):
        if 'user_id' not in request.session:
            messages.error(request, "Please log in or sign up.")
            return redirect('home')
        else:
            book = get_object_or_404(Book, id=id)
            if book.stock > 0:
                book.stock -= 1
                book.save()
                messages.success(request, f"successfully purchased {book.title}.")
                return redirect('home')

class BooksView(View):
    def get(self, request):
        user_info = None
        if 'user_id' in request.session:
            try:
                user_info = UserAccount.objects.get(id=request.session['user_id'])
            except UserAccount.DoesNotExist:
                user_info = None
        all_books = Book.objects.all()
        return render(request, 'books.html', {'all_books': all_books, 'user': user_info})

class GenreView(View):
    def get(self, request):
        user_info = None
        if 'user_id' in request.session:
            try:
                user_info = UserAccount.objects.get(id=request.session['user_id'])
            except UserAccount.DoesNotExist:
                user_info = None
        genres = Book.objects.values_list('genre', flat=True).distinct()
        genre_books = {genre: Book.objects.filter(genre=genre) for genre in genres}
        return render(request, 'genre.html', {'genre_books': genre_books, 'user': user_info})

# def add_to_cart(request, id):
#     if 'user_id' not in request.session:
#         messages.error(request, "Please log in or sign up to add items to your cart.")
#         return redirect('book_detail', id=id)
#     book = get_object_or_404(Book, id=id)
#     cart = request.session.get('cart', [])
#     cart.append({'id': book.id, 'title': book.title, 'price': book.price})
#     request.session['cart'] = cart
#     messages.success(request, "Item added to cart!")
#     return redirect('book_detail', id=id)

