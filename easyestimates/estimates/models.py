from django.db import models
from datetime import datetime


class Item(models.Model):
    item_name = models.CharField(max_length=100)
    item_code = models.CharField(max_length=10, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.item_name

class Unit(models.Model):
    item = models.ForeignKey('Item', on_delete=models.CASCADE)
    unit = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.unit

class Rate(models.Model):
    unit = models.ForeignKey('Unit', on_delete=models.CASCADE)
    item_mrp = models.IntegerField(blank=True, null=True)
    item_rate = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Customers(models.Model):
    customer_name = models.CharField(max_length=30)
    customer_mobile_number = models.CharField(max_length=10, blank=True)
    customer_email_address = models.CharField(max_length=50, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.customer_name

class Estimates(models.Model):
    customers = models.ForeignKey(Customers, on_delete=models.CASCADE)
    estimate_name = models.DateTimeField('Estimate Name', default=datetime.now)
    def __str__(self):
        return self.estimate_name

class Estimate(models.Model):
    estimates = models.ForeignKey(Estimates, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=50)
    item_mrp = models.IntegerField(blank=True, null=True)
    item_rate = models.IntegerField(blank=True, null=True)
    unit = models.CharField(max_length=20)
    quantity = models.IntegerField(default=0)
    amount = models.IntegerField(default=0)
    def __str__(self):
        return self.item_name

class User(models.Model):
    user_name = models.CharField(max_length=50)
