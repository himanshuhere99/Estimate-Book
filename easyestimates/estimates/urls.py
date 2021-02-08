from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_item/', views.add_item, name='add_item'),
    path('list_items/', views.list_items, name='list_items'),
    path('view_item/', views.view_item, name='view_item'),
    path('add_customer/', views.add_customer, name='add_item'),
    path('list_customers/', views.list_customers, name='list_items'),
    path('view_customer/', views.view_customer, name='view_item'),
    path('create_estimate/', views.create_estimate, name='create_estimate'),
    path('list_estimates/', views.list_estimates, name='list_estimates'),
    path('view_estimate/', views.view_estimate, name='view_estimate'),
]
