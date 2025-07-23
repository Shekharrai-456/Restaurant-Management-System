from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import api_view
from .models import *
from .serializer import CategorySerializer
from rest_framework.serializers import ValidationError
# Create your views here. 

@api_view(['GET','POST'])
def category_list(request):
    if request.method == 'GET':
        categories = Category.objects.all() # objects
        serializer = CategorySerializer(categories, many=True) # convert objects to json
        return Response(serializer.data) # objects in json format

    elif request.method == 'POSt':
        serializer = CategorySerializer(data=request.data)
        serializer.is_valid(raise_exception= True)
        serializer.save()
        return Response({
            'message': 'Category created successfully',
        })


@api_view(['GET','DELETE'])
def category_details(request,id):
    category = Category.objects.get(id = id)
    if request.method == 'GET':
        serializer = CategorySerializer(category)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        total = OrderItem.objects.filter(food__category = category).count()
        if total > 0:
            raise ValidationError({
                'error': 'You cannot delete this category because it has orders',
            })
        category.delete()
        return Response({
            'message': 'Category deleted successfully',
        })
    elif request.method == 'PUT':
        serializer = CategorySerializer(data = request.data)
        serializer.is_vaild(raise_exception=True)
        serializer.save()
        return Response(serializer.data)