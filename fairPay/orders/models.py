from django.db import models
from django.db.models import Sum


class Diner(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)
    diner_table = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'diner'


class Product(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product'


class Order(models.Model):
    start_date = models.DateField()
    end_date = models.DateField(null=True)
    diner = models.ForeignKey(Diner, on_delete=models.CASCADE, related_name='diner_orders')
    products = models.ManyToManyField(Product)

    class Meta:
        default_permissions = ()

    @staticmethod
    def get_orders(start_date, end_date):
        if end_date:
            return Order.objects.filter(start_date__gte=start_date, end_date__lte=end_date)
        return Order.objects.filter(start_date__gte=start_date)

    @staticmethod
    def delete_orders(start_date, end_date):
        count_orders_deleted = 0
        if end_date:
            orders = Order.objects.filter(start_date__gte=start_date, end_date__isnull=False, end_date__lte=end_date)
            count_orders_deleted = orders.count()
            orders.delete()
        return count_orders_deleted

    @property
    def check_total(self):
        return self.products.all().aggregate(Sum('price'))['price__sum']
