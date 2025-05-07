from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_product, name='add_product'),
    path('list/', views.list_product, name='list_product'),
    # path('detail/<int:pk>/', views.product_detail, name='product_detail'),
    # path('update/<int:pk>/', views.update_product, name='update_product'),
    # path('delete/<int:pk>/', views.delete_product, name='delete_product'),
]