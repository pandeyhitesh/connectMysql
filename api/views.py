from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from . serializers import ProductSerializer
from . models import Product


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/product-list/',
        'Detail view':'/product-detail/<int:id>',
        'Create': '/product-create/',
        'Update': '/product-update/<int:id>', 
        'Delete': '/product-delete/<int:id>',
    }

    return Response(api_urls)


'''
    APIs for Product
'''
@api_view(['GET'])
def showAll(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def viewProduct(request,pk):
    product = Product.objects.get(id=pk)
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def createProduct(request):
    # product = Product.objects.get(id=pk)

    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def updateProduct(request,pk):
    product = Product.objects.get(id=pk)
    serializer = ProductSerializer(instance=product,data=request.data)
    
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)



@api_view(['GET'])
def deleteProduct(request,pk):
    product = Product.objects.get(id=pk)
    product.delete()
    
    return Response('items deleted successfully')