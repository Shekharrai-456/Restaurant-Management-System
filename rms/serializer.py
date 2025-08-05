from rest_framework import serializers
from .models import *
# converts objects to json -> serializer
# converts json to objects -> deserializer
# class CategorySerializer(serializers.Serializer):
#    id = serializers.IntegerField(read_only = True)
#    name = serializers.CharField()
   
#    def create(self, validated_data):
#       return Category.objects.create(**validated_data)
   
#    def update(self, instance, validated_data):
#       instance.name = validated_data.get('name',instance.name)
#       instance.save()
#       return instance

class CategorySerializer(serializers.ModelSerializer):
   class Meta:
      model = Category
      fields = ['id','name']
      # fields = '__all__'
      # exclude = ['id']
   
   def save(self, **kwargs):
      validated_data = self.validated_data
      # total = Category.objects.filter(name = validated_data.get('name')).count()
      total = self.Meta.model.objects.filter(name = validated_data.get('name')).count()
      if total > 0:
         raise serializers.ValidationError({
            "details":"The Category with this name already exists."
         })
      category = self.Meta.model(**validated_data)  # Category(**validation_data)
      return category

class FoodSerializer(serializers.ModelSerializer):
   price_with_tax = serializers.SerializerMethodField()
   category = serializers.StringRelatedField()
   category_id = serializers.PrimaryKeyRelatedField(
      queryset = Category.objects.all(),
      source = 'category'
   )
   class Meta:
      model = Food
      fields = ['id','name','price','price_with_tax','category_id','category']
   
   def get_price_with_tax(self, food:Food):
      return food.price * 0.13 + food.price

class OrderItemSerializer(serializers.ModelSerializer):
   class Meta:
      model = OrderItem
      fields = ['food']

class OrderSerializer(serializers.ModelSerializer):
   user = serializers.HiddenField(default = serializers.CurrentUserDefault())
   items = OrderItemSerializer(many=True)
   status = serializers.CharField(read_only  = True)
   payment_status = serializers.CharField(read_only  = True)
   class Meta:
      model = Order
      fields = ["id","user","total_price","quantity","status","payment_status","items"]
   
   def create(self, validated_data):
      items = validated_data.pop('items')
      order =  Order.objects.create(**validated_data)
      
      for item in items:
         OrderItem.objects.create(order=order, food = item.get('food'))
      return order
   
# validated_data =: 
# {
#     "total_price": null,
#     "quantity": null,
# }

# items = #     "items": [{"food":20} ]