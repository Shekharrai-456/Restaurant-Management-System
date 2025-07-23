from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import api_view
from .models import Category
from .serializer import CategorySerializer
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

@api_view(['GET','POST'])
def table_list(request):
    if request.method == "GET":
        table = Table.objects.all()
        serializer = TableSerializer(table, many=True)
        return Response (serializer.data)
    elif request.method == 'POST':
        serializer = TableSerializer(data= request.data)
        serializer.is_valid(raise_exception= True)
        serializer.save()
        return Response ({
            "number": "2",
            "size" : "9",
            "available" : True,
        })
        
@api_view(['PUT'])
def table_update(request, id):
    if request.method == "PUT":
        table = Table.objects.get(id=id)
        serializer = TableSerializer(table, data=request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(serializer.data)
    
class SnippetSerializer()

@api_view(['GET'])
def category_details(request,id):
    if request.method == 'GET':
        category = Category.objects.get(id = id)
        serializer = CategorySerializer(category)
        return Response(serializer.data)