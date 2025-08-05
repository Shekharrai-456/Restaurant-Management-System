from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializer import *
from rest_framework.serializers import ValidationError
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters
from django_filters import rest_framework as filter
from .filters import FoodFilter
# from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .permission import IsAuthenticatedOrReadOnly
# Create your views here.

# Api using Viewset
class CategoryViewset(ModelViewSet):
   queryset = Category.objects.all()
   serializer_class = CategorySerializer
   pagination_class = PageNumberPagination
   permission_classes = [IsAuthenticatedOrReadOnly]
   
   
   def destroy(self, request, pk):
      category = Category.objects.get(pk = pk)
      total = OrderItem.objects.filter(food__category = category).count() # count the number of category that is present in the food in OrderItem.
      if total > 0: # if the category is present in the OrderItem then we cannot delete it.
         raise ValidationError({
            "detail":"The food of this category exists in the order."
         })
      category.delete()
      return Response({
         "details":"Category deleted."
      }, status= status.HTTP_404_NOT_FOUND)


class FoodViewset(ModelViewSet):
   queryset = Food.objects.select_related('category').all()
   serializer_class = FoodSerializer
   pagination_class = PageNumberPagination
   filter_backends = [filters.SearchFilter, filter.DjangoFilterBackend]
   search_fields = ['name']
   # filterset_fields = ['category']
   filterset_class = FoodFilter
   permission_classes = [IsAuthenticatedOrReadOnly]

# API for Table

class OrderViewset(ModelViewSet):
   queryset = Order.objects.prefetch_related('items').all()
   serializer_class = OrderSerializer
   pagination_class = PageNumberPagination
   permission_classes = [IsAuthenticatedOrReadOnly]






















# Api creation using Generic and ModelMixin
# class CategoryView(ListAPIView, CreateAPIView):
#    queryset = Category.objects.all()
#    serializer_class = CategorySerializer

# class CategoryDetail(RetrieveAPIView, UpdateAPIView, DestroyAPIView):
#    queryset = Category.objects.all()
#    serializer_class = CategorySerializer
#    lookup_field = 'pk'
   
#    def delete(self, request, pk):
#       category = Category.objects.get(pk = pk)
#       total = OrderItem.objects.filter(food__category = category).count() # count the number of category that is present in the food in OrderItem.
#       if total > 0: # if the category is present in the OrderItem then we cannot delete it.
#          raise ValidationError({
#             "detail":"The food of this category exists in the order."
#          })
#       category.delete()
#       return Response({
#          "details":"Category deleted."
#       }, status= status.HTTP_404_NOT_FOUND)





# Api Creation using APIView
# class CategoryView(APIView):
   # def get(self, request):
   #    category = self.queryset
   #    serializer = self.serializer_class(category , many = True)
   #    return Response(serializer.data)
   
   # def post(self, request):
   #    serializer = CategorySerializer(data = request.data)
   #    serializer.is_valid(raise_exception= True)
   #    serializer.save()
   #    return Response({
   #       'details':'New category added.'
   #    }, status= status.HTTP_201_CREATED)

# class CategoryDetail(APIView):
   # def get(self, request, id):
   #    category = Category.objects.get(id = id)
   #    serializer = CategorySerializer(category)
   #    return Response(serializer.data)
   
   # def put(self, request, id):
   #    category = Category.objects.get(id = id)
   #    serializer = CategorySerializer(category, data = request.data)
   #    serializer.is_valid(raise_exception=True)
   #    serializer.save()
   #    return Response(serializer.data)
   
   # def delete(self, request, id):
   #    category = Category.objects.get(id = id)
   #    total = OrderItem.objects.filter(food__category = category).count() # count the number of category that is present in the food in OrderItem.
   #    if total > 0: # if the category is present in the OrderItem then we cannot delete it.
   #       raise ValidationError({
   #          "detail":"The food of this category exists in the order."
   #       })
   #    category.delete()
   #    return Response({
   #       "details":"Category deleted."
   #    }, status= status.HTTP_404_NOT_FOUND)





# Function based Api view using decorator
# @api_view(['GET','POST'])
# def category_list(request):
#    if request.method == 'GET':
#       category = Category.objects.all()       # objects
#       serializer = CategorySerializer(category , many = True) # convert objects to json
#       return Response(serializer.data) # objects in json format
   
#    elif request.method == 'POST':
#       serializer = CategorySerializer(data = request.data)
#       serializer.is_valid(raise_exception= True)
#       serializer.save()
#       return Response({
#          'details':'New category added.'
#       })

# @api_view(['GET','DELETE','PUT'])
# def category_details(request, id):
#    category = Category.objects.get(id = id)
#    if request.method == 'GET':
#       serializer = CategorySerializer(category)
#       return Response(serializer.data)
   
#    elif request.method == 'DELETE':
#       total = OrderItem.objects.filter(food__category = category).count() # count the number of category that is present in the food in OrderItem.
#       if total > 0: # if the category is present in the OrderItem then we cannot delete it.
#          raise ValidationError({
#             "detail":"The food of this category exists in the order."
#          })
#       category.delete()
#       return Response({
#          "details":"Category deleted."
#       })
   
#    elif request.method == 'PUT':
#       serializer = CategorySerializer(category, data = request.data)
#       serializer.is_valid(raise_exception=True)
#       serializer.save()
#       return Response(serializer.data)


# table view, serializer(table api create)