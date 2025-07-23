from rest_framework import serializers
from .models import Category

# converts objects to json -> serializer
# converts json to objects -> deserializer

class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    
    def create(self, validated_data):
        return Category.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.save()
        return instance
        
    
