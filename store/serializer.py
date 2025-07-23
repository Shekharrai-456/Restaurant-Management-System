from rest_framework import serializers

# converts objects to json -> serializer
# converts json to objects -> deserializer

class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    
