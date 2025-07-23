from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.
class Category(models.Model):
    name = models.CharField( max_length=50)
    
    def _str_ (self):
        return self.name

class Food(models.Model):
    name = models.CharField(max_length=130)
    price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def _str_ (self):
        return self.name

class Table(models.Model):
    number = models.IntegerField()
    size = models.IntegerField()
    available = models.BooleanField(default=False)
    
    def _str_ (self):
        return f"{self.number}- {self.available}"
    
class Order(models.Model):
    PENDING = 'P'
    COMPLETED = 'C'
    STATUS_CHOICE = {
        PENDING : "Pending",
        COMPLETED : "Comleted"
    }
    PAID = "P"
    UNPAID = "U"
    
    PAYMENTS_CHOICE= {
        PAID : "Pending",
        UNPAID : "Unpaid"
    }
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price = models.FloatField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=1, choices = STATUS_CHOICE, default=PENDING)
    payment_status = models.CharField(max_length=1, choices = PAYMENTS_CHOICE, default= UNPAID)
    
    def _str_(self):
        return f"Order{self.user}-{self.status}"

class OrderItems(models.Model):
    order = models.ForeignKey(Order, on_delete= models.PROTECT)
    food = models.ForeignKey(Food, on_delete=models.PROTECT)

 
class Ingredients (models.Model):
    ingredients_id = models.IntegerField()
    name = models.CharField(max_length=90)
    
    def _str_(self):
        return f"{self.ingredients_id}- {self.name}"

class Storage(models.Model):
    storage_id = models.IntegerField()
    ingredients = models.ForeignKey(Ingredients, max_length=10, on_delete = models.PROTECT)
    quantity = models.BooleanField(default=False)
    
    def _str_(self):
        return f"{self.storage_id}-{Ingredients}"
 
class recipe(models.Model):
    CATEGORY_CHOICES = {
        "veg": "Vegetarian",
        "non-veg":"Non_vegetarian",
        "vegan":"Vegan",
        "dessert":"Dessert",
    }
    
    recipe_id = models.IntegerField()
    food = models.ForeignKey(Food, max_length=90, on_delete=models.PROTECT)
    recipe = models.CharField(max_length = 90, choices = CATEGORY_CHOICES,default = "veg")
    
    def _str_ (self):
        return f"{self.food}-{self.recipe}"