from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import (
    MutationCategorySerializer,
    GetCategorySerializer
)

from .models import Category


class CategoriesAPIView(APIView):
    def post(self, request):
        try:
            name = request.data["values"]["name"]

            data = {
                "name": name,
            }

            serializer = MutationCategorySerializer(data=data)
            if serializer.is_valid():
                serializer.save(user=request.user)
                return Response({"data": serializer.data}, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get(self, request):
        try:
            categories = Category.objects.filter(user=request.user)
            serializer = GetCategorySerializer(categories, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class BulkDeleteCategoriesAPIView(APIView):
    def post(self, request):
        try:
            category_ids = request.data["ids"]
            Category.objects.filter(id__in=category_ids, user=request.user).delete()
            return Response({"data": category_ids}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class CategoryByIdAPIView(APIView):
    def get(self, request, pk):
        try:
            category = Category.objects.get(pk=pk, user=request.user)
            serializer = GetCategorySerializer(category)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def patch(self, request, pk):
        try:
            name = request.data["values"]["name"]

            data = {
                "name": name,
            }

            category = Category.objects.get(pk=pk)
            serializer = MutationCategorySerializer(category, data=data, partial=True)
            if serializer.is_valid():
                serializer.save(user=request.user)
                return Response({"data": serializer.data}, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk):
        try:
            Category.objects.get(pk=pk, user=request.user).delete()
            return Response({}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
