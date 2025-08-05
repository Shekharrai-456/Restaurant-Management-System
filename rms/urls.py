from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'categories',CategoryViewset, basename='categories')
router.register(r'foods',FoodViewset, basename='foods')
router.register(r'orders',OrderViewset, basename='orders')

urlpatterns = [
   # path('categories/',CategoryViewset.as_view({'get':'list','post':'create'}), name = 'category'),
   # path('categories/<pk>/',CategoryViewset.as_view({'get':'retrieve','put':'update','patch':'partial_update','delete':'destroy'}))
   # path('categories/', CategoryView.as_view()),
   # path('categories/<pk>/', CategoryDetail.as_view())
   # path('category/',category_list),
   # path('category/<id>/',category_details)
] + router.urls
