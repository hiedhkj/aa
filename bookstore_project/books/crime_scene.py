








#----------- صحنه جُرم ----------
#----------- صحنه جُرم ----------
#----------- صحنه جُرم ----------
#----------- صحنه جُرم ----------
#----------- صحنه جُرم ----------
#----------- صحنه جُرم ----------
#----------- صحنه جُرم ----------





















# import sys
# import os
# import django
# from faker import Faker
# import random

# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bookstore.settings')
# django.setup()

# from books.models import Book

# fake = Faker()

# GENRE_CHOICES = [
#     'fiction', 'non_fiction', 'mystery', 'fantasy', 'biography',
#     'science_fiction', 'romance', 'horror', 'self_help', 'history'
# ]

# def create_books(n):
#     for _ in range(n):
#         book = Book(
#             title=fake.sentence(nb_words=2),
#             author=fake.name(),
#             price=float(random.randint(5 , 99)) + 0.99,
#             rating=0.0,
#             description=fake.text(),
#             published_date=fake.date(),
#             isbn=fake.isbn13(),
#             cover_image=f'https://picsum.photos/200/300?random={random.randint(1, 10000)}',
#             language=fake.language_name(),
#             publisher=fake.company(),
#             genre=random.choice(GENRE_CHOICES),
#             stock=random.randint(1, 10) 
#         )
#         book.save()

# create_books(50)