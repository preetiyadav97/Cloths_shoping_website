from django.shortcuts import render,HttpResponse,redirect
from Buy.admin import Contact,Category,Product,Cart,Wallet
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.views import View
from django.db.models import Count
from django.db.models import Sum
import razorpay
# ---- import for send messages -----
from django.contrib import messages
# ---- import for send email -----
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import EmailMultiAlternatives
# ---- END -------


# Create your views here.
def about(request):
    return render(request,'about.html')




def contact(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        mgs=request.POST['message']
        detail=Contact(name=name,email=email,mgs=mgs)
        detail.save()
        
        #--------
        # details={'name':name,'email':email,'mgs':mgs}
        # subject="Thanks for contacting"
        # html_message=render_to_string("contact.html",details)
        # plain_message=strip_tags(html_message)
        # from_email="k68146369@gmail.com"
        # to= "preetiyadav73703@gmail.com"

        # send_mail(subject,html_message=html_message,plain_message,from_email,to,fail_silently=False)
        send_mail(
          "Thanks for contacting",
           mgs,
          'settings.EMAIL_HOST_USER',
           ['preetiyadav73703@gmail.com'],
           fail_silently=False,
        )
    return render(request,'contact.html')


def index(request):
    man_products=Product.objects.filter(cat__name="Men")
    woman_products=Product.objects.filter(cat__name="women's")
    kid_products=Product.objects.filter(cat__name="Kids")
    user=request.user
    a = user.id
    return render(request,'index.html',{'man_products':man_products,'woman_products':woman_products,'kid_products':kid_products})
     


def product(request):
    man_products=Product.objects.filter(cat__name="Men",permission=True)
    woman_products=Product.objects.filter(cat__name="women's",permission=True)
    kid_products=Product.objects.filter(cat__name="Kids",permission=True)
    return render(request,'products.html',{'man_products':man_products,'woman_products':woman_products,'kid_products':kid_products})



def single(request):
    return render(request,'single-product.html')
    
    
def nav(request):
    return render(request,'show.html')


def signup(request):
    if request.method == 'POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        username=request.POST['username']
        email=request.POST['email']
        gender=request.POST['gender']
        password=request.POST['password']
        confirmpassword=request.POST['confirmpassword']

        user = User.objects.create_user(username,email,password)
        user.first_name=fname
        user.last_name=lname

        user.save()
        return redirect("index1")

    return render(request,'sign.html')



def login_detail(request):
    if request.method =="POST":
        username = request.POST["loginusername"]
        password = request.POST["loginpassword"]
        user = authenticate(username=username, password=password)
        print(user)
        print("==================================")
        if user is not None:
            login(request, user)
            return redirect("index1")
        else:
            return HttpResponse('Not - found pages')
    return render(request,'login.html')



def logout_detail(request):
    logout(request)
    man_products=Product.objects.filter(cat__name="Men")
    woman_products=Product.objects.filter(cat__name="women's")
    kid_products=Product.objects.filter(cat__name="Kids")
    return render(request,'index.html',{'man_products':man_products,'woman_products':woman_products,'kid_products':kid_products})



def add_to_cart(request,pk):
    user=request.user
    a = user.id
    quantity=Cart.objects.filter(user=a).count()
    a=Cart(user_id=user.id,product_id=pk)
    a.save()
    dat=Cart.objects.filter(user=user.id)
    show={'dat':dat,'quantity':quantity}
    return render(request,'single-product.html',show)



from django.conf import Settings
def cart(request,pk):
    user=request.user  
    get_Product = Product.objects.filter(id=pk).annotate(
        is_added_to_Cart = Count("cart")
        )
    print(get_Product.values("is_added_to_Cart"))
    show={'get_Product':get_Product}

    return render(request,"productdetail.html",show) 





# def cartshow(request):
#     user=request.user
#     a = user.id
#     print(a)
#     dat=Cart.objects.filter(user=a)
#     quantity=Cart.objects.filter(user=a).count()
#     print(  quantity)
    
#     show={'dat':dat,"quantity":quantity}
#     print(show)
#     return render(request,'single-product.html',show)


from django.http import JsonResponse
def cartshow(request):
    user = request.user
    a = user.id
    print(a)
    
    # Get all cart items for the user
        
    dat=Cart.objects.filter(user=user.id)
    
    # Calculate the total price of all products in the cart
    total_price = dat.aggregate(total_price=Sum('product__price'))['total_price'] or 0.0
    print("=========")
    print(total_price)
    print("==================")
    quantity =dat.count()
    print(quantity)
    
    print("For payments")
    
    client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
    try:
        razorpay_order = client.order.create({"amount": total_price  , "currency": "INR", "payment_capture": 1})
        print("_____")
        print(razorpay_order)
        dat.update(provider_order_id=razorpay_order['id'])
    except Exception as e :
        return e
        
    
    show = {'dat': dat, 'total_price': total_price, 'quantity': quantity,'razorpay_order':razorpay_order}
    return render(
                request,
                "payment.html",
                {
                    "callback_url": "http://" + "127.0.0.1:8000" + "/razorpay/callback/",
                    "razorpay_key": "rzp_test_k4rElzvZ4GMbO8",
                    "razorpay_order": razorpay_order ,
                },
                show,
            )

def remove (request,pk):
    get_item=Cart.objects.get(id=pk)
    get_item.delete()

    return redirect('Cart')
    
 
def purchase(request):
    client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
    razorpay_order = client.order.create({"amount": 5000 , "currency": "INR", "payment_capture": 1})
    print("_____")
    print(razorpay_order)
    context={'cart':cart,'razorpay_order':razorpay_order}
    return render(request,'single-product.html',context)

def total(request,id):
    user=request.user
    id=user.id
    get_item=Cart.objects.get(user=id)
    if request.method == "POST":
        print("=====================================================")
        quantity= request.POST.get['qty']
        quantity=get_item.quantity
        quantity.save()
        
        print(quantity)
        int_qty=int(quantity)
        print(int_qty)
       
  
        totalprice=0
        for item in get_item:
            totalprice= totalprice + item.product.price*int_qty
            
    show={'get_item':get_item,'totalprice':totalprice}  
    return render(request,'single-product.html',show)