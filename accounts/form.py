from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django import forms
from .models import Order
from .models import customer
from .models import events
from .models import Products
from .models import ContactUS
from .models import CreateBlog


class BlogForm(ModelForm):
    class Meta:
        model = CreateBlog
        fields = ['sno','title', 'content', 'author', 'category']


class CreateUser(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'


class CustomerForm(ModelForm):
    class Meta:
        model = customer
        fields = '__all__'


class EventForm(ModelForm):
    class Meta:
        model = events
        fields = '__all__'
        # exclude = ['id']


class AddProduct(ModelForm):
    class Meta:
        model = Products
        fields = '__all__'
        exclude = ['tags']


class UpdateProduct(ModelForm):
    class Meta:
        model = Products
        fields = '__all__'


class EventUpdate(ModelForm):
    class Meta:
        model = events
        fields = '__all__'


class DeleteEvent(ModelForm):
    class Meta:
        model = events
        fields = '__all__'


class contactform(ModelForm):
    class Meta:
        model = ContactUS
        fields = '__all__'
