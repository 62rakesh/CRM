from django.urls import path
from . import views


urlpatterns = [
    path('index/portfolio/',views.portfolio,name='portfolio'),
    path('index/',views.index,name='index'),
    path('faq/',views.faq,name='faq'),
    path('contactus/',views.Contact,name='contactus'),
    path('',views.home,name='home'),
    path('products/',views.products,name='products'),
    path('customer/<str:pk>/',views.customer1,name='customer'),
    path('order/',views.orders,name='order'),
    path('create_order/',views.CreateOrder,name='create_order'),
    path('update_order/<str:pk>',views.UpdateOrder,name='update_order'),
    path('delete_order/<str:pk>',views.delete,name='delete_order'),
    path('create_customer/',views.CreateCustomer,name='create_customer'),
    path('events/',views.event,name='event'),
    path('update_event/',views.UpdateEvent,name='update_event'),
    path('add_event/',views.AddEvent,name='add_event'),
    path('delete_event/',views.EventDelete,name='delete_event'),
    path('add_product',views.Addproduct,name='add_product'),
    path('delete_product/<str:pk>',views.DeleteProduct,name='delete_product'),
    path('update_product/<str:pk>',views.ProductUpdate,name='update_product'),
    path('delete_query/',views.DeleteQuery,name='delete_query'),


    # CUSTOMER LOGIN URL SETUP

    path('login/',views.loginPage,name='login'),
    path('logout/',views.logoutUser,name='logout'),
    path('register/',views.registerPage,name='register'),

    # BLOG PAGE SETUP
    path('blog/',views.blog,name='blog'),
    path('delete_blog/',views.DeleteBlog,name='delete_blog'),








    # CUSTOMER PAGE SETUP

    path('user/',views.user,name='create_user')


]