# from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib import messages
# from books.models import Book

# def add_to_cart(request, id):
#     # if 'user_id' not in request.session:
#     #     messages.error(request, "Please log in or sign up to add items to your cart.")
#     #     return redirect('book_detail', id=id)
#     book = get_object_or_404(Book, id=id)
#     cart = request.session.get('cart', [])
#     cart.append({'id': book.id, 'title': book.title, 'price': book.price})
#     request.session['cart'] = cart
#     messages.success(request, "Item added to cart!")
#     return redirect('book_detail', id=id)
