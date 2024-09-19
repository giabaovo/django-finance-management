from django.urls import path

from .api import EmailTokenObtainPairView, HelloWorld

urlpatterns = [
    path('token/', EmailTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('', HelloWorld.as_view(), name='token_obtain_pair')
]
