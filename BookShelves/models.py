from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    BookName = models.CharField(max_length=100)
    Author = models.CharField(max_length=100)
    Rating = models.IntegerField(default=0)
    Pages = models.IntegerField(default=0)
    Checked = models.BooleanField()
    def __str__(self):
        return self.BookName + " | " + self.Author