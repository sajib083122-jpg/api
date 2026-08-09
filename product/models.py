from django.db import models

# Create your models here.

class Book(models.Model):
    book_name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    cover_image = models.ImageField(upload_to='book_covers/', null=True, blank=True)  # ✅ নতুন ফিল্ড
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)


    def __str__(self):                 # string Re-presentation at admin pannle
        return self.book_name