from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('items/', views.items, name='items'),
    path('items/create/', views.create_item, name='create_item'),
    path('items/update/<int:item_id>/', views.update_item, name='update_item'),
    path('items/delete/<int:item_id>/', views.delete_item, name='delete_item'),
    path('categories/', views.categories, name='categories'),
    path('categories/create/', views.create_category, name='create_category'),
    path('categories/update/<int:category_id>/', views.update_category, name='update_category'),
    path('categories/delete/<int:category_id>/', views.delete_category, name='delete_category'),
    path('suppliers/', views.suppliers, name='suppliers'),
    path('suppliers/create/', views.create_supplier, name='create_supplier'),
    path('suppliers/update/<int:supplier_id>/', views.update_supplier, name='update_supplier'),
    path('suppliers/delete/<int:supplier_id>/', views.delete_supplier, name='delete_supplier'),
]