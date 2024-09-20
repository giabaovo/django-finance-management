from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import (
    MutationAccountSerializer,
    GetAccountSerializer
)

from .models import Account


class AccountsAPIView(APIView):
    def post(self, request):
        try:
            name = request.data["values"]["name"]

            data = {
                "name": name,
            }

            serializer = MutationAccountSerializer(data=data)
            if serializer.is_valid():
                serializer.save(user=request.user)
                return Response({"data": serializer.data}, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get(self, request):
        try:
            accounts = Account.objects.filter(user=request.user)
            serializer = GetAccountSerializer(accounts, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class BulkDeleteAccountsAPIView(APIView):
    def post(self, request):
        try:
            account_ids = request.data["ids"]
            Account.objects.filter(id__in=account_ids, user=request.user).delete()
            return Response({"data": account_ids}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class AccountByIdAPIView(APIView):
    def get(self, request, pk):
        try:
            account = Account.objects.get(pk=pk, user=request.user)
            serializer = GetAccountSerializer(account)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def patch(self, request, pk):
        try:
            name = request.data["values"]["name"]

            data = {
                "name": name,
            }

            account = Account.objects.get(pk=pk)
            serializer = MutationAccountSerializer(account, data=data, partial=True)
            if serializer.is_valid():
                serializer.save(user=request.user)
                return Response({"data": serializer.data}, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk):
        try:
            Account.objects.get(pk=pk, user=request.user).delete()
            return Response({}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
