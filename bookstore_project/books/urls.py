from django.urls import path
from .views import BookDetailView, BuyNowView, BooksView , GenreView
# from orders.views import add_to_cart

urlpatterns = [
    path('', BooksView.as_view(), name='booksd'),
    path('genre/', GenreView.as_view(), name='genre'),
    path('<int:id>/', BookDetailView.as_view(), name='book_detail'),
    path('buy_now/<int:id>/', BuyNowView.as_view(), name='buy_now'),
    # path('add_to_cart/<int:id>/', add_to_cart, name='add_to_cart'),
]