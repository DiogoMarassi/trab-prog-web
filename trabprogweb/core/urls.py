from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_items, name='list_item'),
    path('new/', views.create_items, name='create_item'),
    path('edit/<int:id>/', views.edit_items, name='edit_item'),
    path('delete/<int:id>/', views.delete_items, name='delete_item'),
]