from django.db import models
# Create your models here.
from django.db.models import ManyToManyField
from django.contrib.auth.models import User


class CreateBlog(models.Model):
    objects = None
    CATEGORY = (
        ('Sports', 'Sports'),
        ('Travel', 'Travel'),
        ('Coding', 'Coding'),
        ('Solo Trip', 'Solo Trip'),
        ('Food', 'Food'),

    )
    sno = models.IntegerField(null=True)
    title = models.CharField(max_length=255, null=True)
    content = models.TextField()
    author = models.CharField(max_length=13, null=True)
    created_date = models.DateTimeField(auto_now=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)

    def __str__(self):
        return self.title


class customer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    id = models.FloatField(primary_key=True)
    date_created = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Products(models.Model):
    objects = None
    CATEGORY = (
        ('Hardware', 'Hardware'),
        ('Software', 'Software'),
        ('Food & Beverage', 'Food & Beverage'),
        ('Indoor', 'Indoor'),
        ('Outdoor', 'Outdoor'),
    )
    product_name = models.CharField(max_length=200, null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    price = models.FloatField(null=True)
    description = models.CharField(max_length=200, null=True)
    date_created = models.DateField(auto_now_add=True, null=True)
    tags = ManyToManyField(Tag)

    def __str__(self):
        return self.product_name


class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered'),
    )
    customer = models.ForeignKey(customer, null=True, on_delete=models.SET_NULL)
    Products = models.ForeignKey(Products, null=True, on_delete=models.SET_NULL)
    date_created = models.DateField(auto_now_add=True, null=True)
    address = models.CharField(max_length=200, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    note = models.CharField(max_length=300, null=True)

    def __str__(self):
        return str(self.Products)


class events(models.Model):
    objects = None
    category = (
        ('Birthday event', 'Birthday event'),
        ('Office event', 'Office event'),
        ('Team event', 'Team event'),
        ('House event', 'House event'),
    )
    id = models.FloatField(primary_key=True)
    event_name = models.CharField(max_length=200, null=True)
    event_category = models.CharField(max_length=200, null=True, choices=category)
    date_created = models.DateField(auto_now_add=True, null=True)
    details = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.event_name


# class contact(models.Model):

class ContactUS(models.Model):
    objects = None
    first_name = models.CharField(max_length=200, null=True)
    email_address = models.CharField(max_length=200, null=True)
    phone_number = models.CharField(max_length=15, null=True)
    query = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.first_name
