from django.urls import path

from .api import (
    AccountsAPIView,
    BulkDeleteAccountsAPIView,
    AccountByIdAPIView,
)

urlpatterns = [
    path('', AccountsAPIView.as_view(), name='accounts'),
    path('bulk-delete/', BulkDeleteAccountsAPIView.as_view(), name='bulk-delete-account'),
    path('<uuid:pk>/', AccountByIdAPIView.as_view(), name='account-by-id'),
]
