from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
from applications.product.models import Product
User = get_user_model()

class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='commets')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"Comment by {self.author} on {self.product}"

