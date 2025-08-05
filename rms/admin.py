from django.contrib import admin
from .models import *
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
   list_display = ('id',"name")
admin.site.register(Category, CategoryAdmin)

class FoodAdmin(admin.ModelAdmin):
   list_display = ('id',"name","price","category")
   list_filter = ('category',)
   search_fields = ('name','price','category__name')
   list_per_page = 10
   # autocomplete_fields = ('category',)

admin.site.register(Food, FoodAdmin)

class TableAdmin(admin.ModelAdmin):
   list_display = ('number','size','available')
   list_filter = ('size','available')
   list_editable = ('available',)

admin.site.register(Table, TableAdmin)

class OrderItemInline(admin.TabularInline):
   model = OrderItem
   autocomplete_fields = ['food']

class OrderAdmin(admin.ModelAdmin):
   list_display = ('user','quantity','status','payment_status')
   list_filter = ('user','status','payment_status')
   search_fields = ('user',)
   list_editable = ('status','payment_status')
   inlines = [OrderItemInline]
   
admin.site.register(Order, OrderAdmin)

# class OrderItemAdmin(admin.ModelAdmin):
#    list_display = ('id','order','food')
   
# admin.site.register(OrderItem, OrderItemAdmin)