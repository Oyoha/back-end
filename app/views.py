import csv
from os.path import exists
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView
from .forms import ProductForm
from .models import Products
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

FILE_NAME = "file.csv"
ATTACHMENT_CSV = f'attachment; filename={FILE_NAME}'


class ProductsCreateView(SuccessMessageMixin, CreateView):
    template_name = 'products_create.html'
    form_class = ProductForm
    success_url = '/'

    def post(self, request, *args, **kwargs):
        self.success_message = f'Добавлена запись ID={Products.objects.all().values("id").last()["id"]}'
        print(Products.objects.all())
        if not exists(FILE_NAME):
            create_file(FILE_NAME)
        else:
            with open(FILE_NAME, 'a', newline='', encoding='UTF-8') as csv_file:
                writer = csv.writer(csv_file, delimiter=';')
                user = Products.objects.all().values_list('id', 'name', 'weight', 'color').last()
                writer.writerow(user)
        return super().post(request, *args, **kwargs)


def export_product_csv(request):
    create_file(FILE_NAME)
    with open(FILE_NAME, 'r', encoding='UTF-8') as f:
        response = HttpResponse(f.read(), content_type='text/csv')
        response['Content-Disposition'] = ATTACHMENT_CSV
        return response


def create_file(name):
    if not exists(name):
        with open(FILE_NAME, 'a', newline='', encoding='UTF-8') as csv_file:
            writer = csv.writer(csv_file, delimiter=';')
            users = Products.objects.all().values_list('id', 'name', 'weight', 'color')
            for user in users:
                writer.writerow(user)