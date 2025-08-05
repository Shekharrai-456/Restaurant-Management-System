from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.
class Category(models.Model):
   name = models.CharField(max_length=50)
   
   def __str__(self):
      return self.name

class Food(models.Model):
   name = models.CharField(max_length=150)
   price = models.FloatField()
   category = models.ForeignKey(Category, on_delete = models.CASCADE,)
   
   def __str__(self):
      return self.name

class Table(models.Model):
   number = models.IntegerField()
   size = models.IntegerField()
   available = models.BooleanField(default = False)
   
   def __str__(self):
      return f"{self.number}- {self.available}"

class Order(models.Model):
   PENDING = "P"
   COMPLETED = "C"
   STATUS_CHOICE = {
      PENDING :"Pending",
      COMPLETED :"Completed"
   }
   PAID = "P"
   UNPAID = "U"
   
   PAYMENT_CHOICE = {
      PAID :"Pending",
      UNPAID : "Unpaid"
   }
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   total_price = models.FloatField()
   quantity = models.IntegerField()
   status = models.CharField(max_length=1 , choices=STATUS_CHOICE ,default=PENDING, null=True, blank =True)
   payment_status = models.CharField(max_length=1, choices=PAYMENT_CHOICE, default= UNPAID, null=True, blank =True)
   
   def __str__(self):
      return f"Order {self.id}"

class OrderItem(models.Model):
   order = models.ForeignKey(Order, on_delete= models.PROTECT, related_name='items')
   food = models.ForeignKey(Food, on_delete=models.PROTECT, related_name='items')