from django.urls import path
from . import views

urlpatterns = [
    path('add_p/', views.add_product, name='add_product'),
    path('add_c/', views.add_category, name='add_category'),
    path('list_p/', views.list_product, name='products'),
    path('list_c/', views.list_category, name='categories'),
    # path('detail/<int:pk>/', views.product_detail, name='product_detail'),
    # path('update/<int:pk>/', views.update_product, name='update_product'),
    # path('delete/<int:pk>/', views.delete_product, name='delete_product'),
]