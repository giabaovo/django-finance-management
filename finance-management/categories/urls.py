from django.urls import path

from .api import (
    CategoriesAPIView,
    BulkDeleteCategoriesAPIView,
    CategoryByIdAPIView,
)

urlpatterns = [
    path('', CategoriesAPIView.as_view(), name='categories'),
    path('bulk-delete/', BulkDeleteCategoriesAPIView.as_view(), name='bulk-delete-category'),
    path('<uuid:pk>/', CategoryByIdAPIView.as_view(), name='category-by-id'),
]
