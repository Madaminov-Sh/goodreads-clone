from rest_framework.views import APIView, status
from rest_framework.response import Response


from .models import Book
from .serializers import BookSerializer


class BookListsApiView(APIView):
    def get(self, request):
        try:
            books = Book.objects.all()
            serializer = BookSerializer(books, many=True)
            return Response({
                "success": True,
                "data": serializer.data,
                "status": status.HTTP_200_OK
            })
        except Book.DoesNotExist:
            return Response({'error': "Book does not exist", "status": status.HTTP_400_BAD_REQUEST})



class BookDetailAPIView(APIView):
    def get(self, requset, id):
        try:
            book = Book.objects.get(id=id)
            serializer = BookSerializer(book)
            return Response(
                {
                    "access": True,
                    "status": status.HTTP_200_OK,
                    "data": serializer.data
                }
            )
        except Book.DoesNotExist:
            return Response({"error message": "Not found", "status": status.HTTP_400_BAD_REQUEST})