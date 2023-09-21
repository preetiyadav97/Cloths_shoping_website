from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=400)
    email=models.EmailField()
    mgs=models.TextField()
    
    def __str__(self):
        return self.name


class Category(models.Model):
    name=models.CharField(max_length=40)

    def __str__(self):
        return self.name
    

class Product(models.Model):
    cat=models.ForeignKey(Category,on_delete=models.CASCADE)
    name=models.CharField(max_length=500)
    price=models.FloatField(null=True,blank=True)
    image=models.ImageField(upload_to="static/assets/img")
    desc=models.CharField(max_length=500)
    quantity = models.PositiveIntegerField(verbose_name='quantity')
    permission=models.BooleanField(default=False,null=None,blank=None)
    
    

    def __str__(self):
        return self.name


CHOICES = (
    ("1", "Process"),
    ("2", "Completed"),
)

  
CHOICES_PAY = (
   ('SUCCESS' ,"Success"),
   ('FAILURE' , "Failure"),
   ('PENDING' , "Pending"),

)
class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    choices = models.CharField(
        max_length = 20,
        choices = CHOICES,
        default = '1'
        )
    status = models.CharField(
        _("Payment Status"),
        choices = CHOICES_PAY,
        default='PENDING',
        max_length=254,
        blank=False,
        null=False,
    )
    provider_order_id = models.CharField(
        _("Order ID"), max_length=40, null=False, blank=False
    )
    payment_id = models.CharField(
        _("Payment ID"), max_length=36, null=False, blank=False
    )
    signature_id = models.CharField(
        _("Signature ID"), max_length=128, null=False, blank=False
    )
    
#  quantity = models.PositiveIntegerField(verbose_name='quantity')
    # def __str__(self):
    #     return self.user

    
    

class Wallet(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    amount=models.FloatField(null=True,blank=True)

    def __str__(self):
        return self.user
    

  
CHOICES = (
   ('SUCCESS' ,"Success"),
   ('FAILURE' , "Failure"),
   ('PENDING' , "Pending"),

)


class Order(models.Model):
    user =models.ForeignKey(User,on_delete=models.CASCADE,max_length=254, blank=False, null=False)
    amount = models.FloatField(_("Amount"), null=False, blank=False)
    status = models.CharField(
        _("Payment Status"),
        choices = CHOICES,
        default='PENDING',
        max_length=254,
        blank=False,
        null=False,
    )
    provider_order_id = models.CharField(
        _("Order ID"), max_length=40, null=False, blank=False
    )
    payment_id = models.CharField(
        _("Payment ID"), max_length=36, null=False, blank=False
    )
    signature_id = models.CharField(
        _("Signature ID"), max_length=128, null=False, blank=False
    )

    def __str__(self):
        return f"{self.id}-{self.name}-{self.status}"
    



    
# class Image(models.Model):
#     name=models.CharField(max_length=500)
#     price=models.FloatField(null=True, blank=True)
#     image=models.ImageField(upload_to="static/assets/img")
#     # rating = models.IntegerField(default=0)

#     def __str__(self):
#         return self.name


    

