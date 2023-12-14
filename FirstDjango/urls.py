
# from django.contrib import admin
from django.urls import path
from MaiinApp import views

urlpatterns = [
    path('', views.home),
    path('about', views.about),
    path('item/<int:id>', views.get_item, name='item-detail'),
    path('items', views.items_list, name='items-list')
]
