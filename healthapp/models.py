from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=20)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='media/')
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=255)


    def __str__(self):
        return self.title


class News(models.Model):
    date = models.DateField()
    news_title = models.CharField(max_length=200)
    news_image = models.ImageField(upload_to='media/')
    description = models.TextField()
    autor = models.CharField(max_length=20)
    depart = models.CharField(max_length=200)

    def __str__(self):
        return self.news_title

class Booking(models.Model):
    book_name = models.CharField(max_length=50)
    book_email = models.EmailField()
    book_date = models.DateField()
    book_phn = models.CharField(max_length=20)
    book_dep = models.ForeignKey(Department, on_delete=models.CASCADE)
    book_desc = models.TextField(max_length=500)

    def __str__(self):
        return self.book_name

