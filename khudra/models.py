
 
from django.db import models


class Customer(models.Model):
	name = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.name



class Outlet(models.Model):
    name = models.CharField(max_length=225)

    def __str__(self):
        return f'{self.name}'



class List(models.Model):
    outlet = models.ForeignKey(Outlet, on_delete=models.CASCADE)
    number_of_items =  models.CharField(max_length=10)
    replace_items =  models.CharField(max_length=10)
    date = models.DateTimeField(auto_now_add=True,  null=True)
    total_price = models.FloatField()
    paid_list = models.BooleanField(default=False)


class Debts(models.Model):
     outlet = models.ForeignKey(Outlet, on_delete=models.CASCADE)
     list = models.ForeignKey(List, on_delete=models.CASCADE)


class Order(models.Model):
	STATUS = (
			('Pending', 'Pending'),
			('Out for delivery', 'Out for delivery'),
			('Delivered', 'Delivered'),
			)
    
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	name = models.ForeignKey(Customer, null=True, on_delete=models.CASCADE)
	status = models.CharField(max_length=200, null=True, choices=STATUS)
	note = models.CharField(max_length=1000, null=True)
    customer = models.ForeignKey(Customer, null=True, on_delete= models.SET_NULL)
	



