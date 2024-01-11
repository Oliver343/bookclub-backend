from rest_framework.response import Response
from rest_framework.decorators import api_view
from books.models import Book
from .serializers import ItemSerializer

@api_view(['GET'])
def getData(request):
    books = Book.objects.all()
    serializer = ItemSerializer(books, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addItem(request):
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def delItem(request):
    books = Book.objects.all().delete()
    books.save()
    return Response(books)
