# select all the records from the Customer table
from accounts.models import *

customer = customer.objects.all()
# print(customer)
# selct first customer from the customer table
FirstCustomer = customer.objects.first()
# print(FirstCustomer)
# select last customer from the customer table
LastCustomer = customer.objects.last()
# print(LastCustomer)

# Return single customer by name
customerByName = customer.objects.get(name='Rakesh')
# print(customerByName)
# Return single customer by id
customerById = customer.objects.get(id='10')
# print(customerById)

# Return all the orders related to customer(variable FirstCustomer is given)
FirstCustomer.order_set.all()

# Return orders customer

