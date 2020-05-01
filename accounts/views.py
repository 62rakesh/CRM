from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .models import *
from .form import OrderForm
from .form import contactform
from .form import CustomerForm
from .form import EventForm
from .form import BlogForm
from .filter import OrderFilter
from .filter import ProductFilter
from .form import AddProduct
from .form import UpdateProduct, CreateUser
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DeleteView


def blog(request):
    post = CreateBlog.objects.all()
    form = BlogForm()
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'post': post,
               'form': form}
    return render(request, 'accounts/blog.html', context)


def index(request):
    return render(request, 'accounts/index.html')


def portfolio(request):
    return render(request, 'accounts/portfolio.html')


def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'username OR password is incorrect')

    return render(request, 'accounts/login.html')


def logoutUser(request):
    logout(request)
    return redirect('login')


def registerPage(request):
    form = CreateUser()
    if request.method == "POST":
        form = CreateUser(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account is created for ' + user)
            return redirect('login')
    context = {'form': form}
    return render(request, 'accounts/register.html', context)


@login_required(login_url='login')
def home(request):
    orders = Order.objects.all()
    customers = customer.objects.all()
    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    order_pending = orders.filter(status='Pending').count()

    context = {'orders': orders, 'customers': customers,
               'total_orders': total_orders, 'delivered': delivered,
               'order_pending': order_pending}

    return render(request, 'accounts/dashboard.html', context)


@login_required(login_url='login')
def products(request):
    products = Products.objects.all()
    prodFilter = ProductFilter(request.GET, queryset=products)
    return render(request, 'accounts/products.html', {'products': products, 'prodFilter': prodFilter})


@login_required(login_url='login')
def ProductUpdate(request, pk):
    product_update = Products.objects.get(id=pk)
    form = UpdateProduct(instance=product_update)
    if request.method == "POST":
        form = UpdateProduct(request.POST, instance=product_update)
        if form.is_valid():
            form.save()
            return redirect('products')
    context = {'form': form, 'product': product_update}
    return render(request, 'accounts/productupdate.html', context)


@login_required(login_url='login')
def DeleteProduct(request, pk):
    product_delete = Products.objects.get(id=pk)
    if request.method == "POST":
        product_delete.delete()
        return redirect('products')
    context = {'product': product_delete}
    return render(request, 'accounts/deleteproduct.html', context)


@login_required(login_url='login')
def customer1(request, pk):
    customers = customer.objects.get(id=pk)
    orders = customers.order_set.all()
    order_count = orders.count()
    myFilter = OrderFilter(request.GET, queryset=orders)
    orders = myFilter.qs
    context = {'customers': customers, 'orders': orders,
               'order_count': order_count,
               'myFilter': myFilter,
               }
    return render(request, 'accounts/customer.html', context)


@login_required(login_url='login')
def orders(request):
    order_delivered = Order.objects.filter(status='Delivered')
    pending_order = Order.objects.filter(status='Pending')
    context = {'order_delivered': order_delivered,
               'pending_order': pending_order}
    return render(request, 'accounts/orders.html', context)


@login_required(login_url='login')
def CreateOrder(request):
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        # print('Printing POST:' ,request.POST)

    context = {'form': form}
    return render(request, 'accounts/order_form.html', context)


def UpdateOrder(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'accounts/order_form.html', context)


def delete(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == "POST":
        order.delete()
        return redirect('/')
    context = {'item': order}
    return render(request, 'accounts/delete.html', context)


@login_required(login_url='login')
def CreateCustomer(request):
    form = CustomerForm()
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'accounts/customer_form.html', context)


@login_required(login_url='login')
def event(request):
    event1 = events.objects.all()
    context = {'event1': event1}
    return render(request, 'accounts/events.html', context)


def UpdateEvent(request):
    context = {}
    return render(request, 'accounts/updateevent.html', context)


def AddEvent(request):
    event1 = events.objects.all()
    form = EventForm()
    if request.method == "POST":
        form = EventForm(request.POST, event1)
        if form.is_valid():
            form.save()
            print("Event Saved Successfully")
            return redirect('event')
        print("Event Saved Successfully")
    context = {'form': form}
    return render(request, 'accounts/addevent.html', context)


def EventDelete(request):
    context = {}
    return render(request, 'accounts/eventdelete.html', context)


def Addproduct(request):
    products = Products.objects.all()
    form = AddProduct()
    if request.method == "POST":
        form = AddProduct(request.POST, products)
        if form.is_valid():
            form.save()
            return redirect('products')
    context = {'form': form}
    return render(request, 'accounts/addproduct.html', context)


# CREATE USER HERE
@login_required(login_url='login')
def user(request):
    orders = request.user.cutomer.order_set.all()
    context = {'orders': orders}
    return render(request, 'accounts/user.html', context)


def Contact(request):
    contact1 = ContactUS.objects.all()
    form = contactform()
    if request.method == "POST":
        form = contactform(request.POST, contact1)
        if form.is_valid():
            form.save()
            messages.success(request, 'A query has been raised against the product.')
            print("A query has been raised against the product.")
    context = {'contact1': contact1,
               'form': form}
    return render(request, 'accounts/contactform.html', context)


def faq(request):
    context = {}
    return render(request, 'accounts/FAQ.html', context)


def DeleteQuery(request):
    query = ContactUS.objects.all()
    first_name = ContactUS.objects.get()
    if request.method == "POST":
        query.delete()
        return redirect('contactus')
    print("A query is deleted.")
    context = {'query': query,
               'first_name': first_name}
    return render(request, 'accounts/deletequery.html', context)


def DeleteBlog(request):
    blog = CreateBlog.objects.all()
    title = CreateBlog.objects.get()
    if request.method == "POST":
        blog.delete()
        return redirect('blog')
    context = {'blog':blog,
               'title':title}
    return render(request,'accounts/deleteblog.html',context)
