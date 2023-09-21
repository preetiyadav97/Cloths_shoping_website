from django.contrib import admin
from .models import Contact,Category,Product,Cart,Wallet,Order
# Register your models here.

# Contact-------

class ContactAdmin(admin.ModelAdmin):
    model=Contact
    list_display=['name','email','mgs']
admin.site.register(Contact,ContactAdmin)

# Category-------

admin.site.register(Category)
admin.site.register(Order)

# Produc-------

class ProductAdmin(admin.ModelAdmin):
    model=Product
    list_display=['name','price','image','permission']
admin.site.register(Product,ProductAdmin)


#  Cart-------
admin.site.register(Cart)

# Wallet------


class WalletAdmin(admin.ModelAdmin):
    model=Wallet
    list_display=['user','amount']
admin.site.register(Wallet,WalletAdmin)