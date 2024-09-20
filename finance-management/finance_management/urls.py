from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/', include('authenticate.urls')),
    path('api/account/', include('accounts.urls')),
    path('api/category/', include('categories.urls')),
]
