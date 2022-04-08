from django.urls import path
from .views import ProductsCreateView, export_product_csv

urlpatterns = [
    path('', ProductsCreateView.as_view()),
    path('export', export_product_csv, name='export_product_csv')
    ]
