from datetime import datetime

from django.contrib.auth.models import User
from django.db import models


from product.models import Product
from customer.models import Customer
import secrets



class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity


# class UniqueCodes(models.Model):
#     code = models.CharField(max_length=8, blank=True, null=True, unique=True)

    # @classmethod
    # def post_create(cls, sender, instance, created, *args, **kwargs):
    #     # If new database record
    #     if created:
    #         # We have the primary key (ID Field) now so let's grab it
    #         id_string = str(instance.id)
    #         # Define our random string alphabet (notice I've omitted I,O,etc. as they can be confused for other characters)
    #         upper_alpha = "ABCDEFGHJKLMNPQRSTVWXYZ"
    #         # Create an 8 char random string from our alphabet
    #         random_str = "".join(secrets.choice(upper_alpha) for i in range(8))
    #         # Append the ID to the end of the random string
    #         instance.code = (random_str + id_string)[-8:]
    #         # Save the class instance
    #         instance.save()
    #
    # def __str__(self):
    #     return "%s" % (self.code,)


class code(models.Model):
    @staticmethod
    def random_str():
        upper_alpha = "ABCDEFGHJKLMNPQRSTVWXYZ"
        # Create an 8 char random string from our alphabet
        random_str = "".join(secrets.choice(upper_alpha) for i in range(8))
        return random_str

    user = models.ForeignKey(User,on_delete=models.CASCADE)
    code = models.CharField(default=random_str.__func__,max_length=10)
    date = models.DateField()

    def check_date(self):
        date = datetime.now()
        return date > self.date

