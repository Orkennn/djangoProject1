# api/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Product, Category, Order, User
from .serializers import ProductSerializer, CategorySerializer, OrderSerializer, UserSerializer

class ProductListView(APIView):
    def get(self, request, format=None):
        products = Product.objects.filter(is_active=True, quantity__gt=0)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_product(request, product_id):
    try:
        product = Product.objects.get(pk=product_id)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def login(request):

    pass

@api_view(['POST'])
def register(request):

    pass

@api_view(['GET'])
def get_categories(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_products_by_category(request, category_id):
    products = Product.objects.filter(category_id=category_id)
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def buy_product(request, product_id):

    pass

@api_view(['POST'])
def get_orders(request, user_id):

    pass