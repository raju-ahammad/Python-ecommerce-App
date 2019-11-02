from django.urls import path
from . import views

urlpatterns = [

    path('order/', views.order_create, name='order'),
    path('admin/order/<int:order_id>/', views.admin_order_detail, name='admin_order_detail'),
    path('admin/order/<int:order_id>/pdf/', views.admin_order_pdf, name='admin_order_pdf'),


]
