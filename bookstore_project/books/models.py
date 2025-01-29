from django.db import models

class Book(models.Model):
    GENRE_CHOICES = [
        ('fiction', 'Fiction'),
        ('non_fiction', 'Non-Fiction'),
        ('mystery', 'Mystery'),
        ('fantasy', 'Fantasy'),
        ('biography', 'Biography'),
        ('science_fiction', 'Science Fiction'),
        ('romance', 'Romance'),
        ('horror', 'Horror'),
        ('self_help', 'Self Help'),
        ('history', 'History'),
    ]

    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    description = models.TextField()
    published_date = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)
    cover_image = models.ImageField(upload_to='covers/')
    language = models.CharField(max_length=30)
    publisher = models.CharField(max_length=100)
    genre = models.CharField(max_length=50, choices=GENRE_CHOICES)
    stock = models.PositiveIntegerField(default=0)
