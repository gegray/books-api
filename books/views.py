from rest_framework import status 
from rest_framework.decorators import api_view 
from rest_framework.response import Response 
from books.models import Books 
from books.serializers import BooksSerializer

@api_view(['GET', 'POST'])
def books_list(request, format=None):
	"""
	List all books, or create a new book.
	"""
	if request.method == 'GET':
		books = Books.objects.all()
		serializer = BooksSerializer(books, many=True)
		return Response(serializer.data)

	elif request.method == 'POST':
		serializer = BooksSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE']) 
def books_detail(request, pk, format=None):
	"""
	Retrieve, update or delete a book instance.
	"""
	try:
		book = Books.objects.get(pk=pk)
	except Books.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		serializer = BooksSerializer(book)
		return Response(serializer.data)

	elif request.method == 'PUT':
		serializer = BooksSerializer(book, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	elif request.method == 'DELETE':
		book.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)