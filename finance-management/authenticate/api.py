from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import CustomUser
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import CustomTokenObtainPairSerializer


class EmailTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        data = request.data

        data['email'] = data['email']['emailAddress']
        data['user_id'] = data['userId']

        email = data['email']
        user_id = data['user_id']
        username = email.split('@')[0]

        user = CustomUser.objects.filter(email=email).first()
        if not user:
            CustomUser.objects.create_user(id=user_id, username=username, email=email)

        serializer = CustomTokenObtainPairSerializer()
        res = serializer.validate(attrs=data)
        print(res)
        return JsonResponse(res)


class HelloWorld(APIView):
    def get(self, request):
        return Response({'message': 'Hello World!'})
