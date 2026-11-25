from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)
    
    class Meta:
        ordering = ['name',]
        verbose_name_plural = "Categories"
        
    def __str__(self):
        return self.name
    
class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField()
    is_solid = models.BooleanField(default=True)
    is_sold = models.BooleanField(default=False)
    image = models.ImageField(upload_to='item_images', null=True, blank=True)
    category = models.ForeignKey(Category, related_name='item', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name='item', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
        
        
    
