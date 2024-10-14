from django.db.models import Count
from django.http import JsonResponse
from django.shortcuts import render,redirect
from django.views import View
from .models import Customer, Product,Cart,OrderPlaced,Wishlist
from .forms import CustomerProfileForm ,CustomerRegistrationForm
from  django.contrib import messages
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# Create your views here.
@login_required
def home(request):
    totalitem=0
    wishitem=0
    if request.user.is_authenticated:
         totalitem = len(Cart.objects.filter(user=request.user))
         totalitem = len(Wishlist.objects.filter(user=request.user))
    return render(request,"app/home.html",locals())

@login_required
def about(request):
    totalitem = 0
    wishitem=0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))  # Corrected from filters to filter
        totalitem = len(Wishlist.objects.filter(user=request.user))
    return render(request, "app/about.html", locals())
@login_required
def contact(request):
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))  # Corrected from filters to filter
        totalitem = len(Wishlist.objects.filter(user=request.user))

    return render(request, "app/contact.html", locals())

@method_decorator(login_required,name='dispatch')
class CategoryView(View):
    def get(self,request,val):
        totalitem=0
        if request.user.is_authenticated:
         totalitem = len(Cart.objects.filter(user=request.user))
        product= Product.objects.filter(category=val)
        title = Product.objects.filter(category=val).values('title')
        totalitem = len(Wishlist.objects.filter(user=request.user))
        return render(request,"app/category.html",locals())
    
@method_decorator(login_required,name='dispatch')
class CategoryTitle(View):
     def get(self,request,val):
        totalitem=0
        wishitem=0
        if request.user.is_authenticated:
         totalitem = len(Cart.objects.filter(user=request.user))
        product= Product.objects.filter(title=val)
        title = Product.objects.filter(category=product[0].category).values('title')
        totalitem = len(Wishlist.objects.filter(user=request.user))
        return render(request,"app/category.html",locals())
    
    
@method_decorator(login_required,name='dispatch')     
class ProductDetail(View):
    def get(self,request,pk):
        product= Product.objects.get(pk=pk)
        totalitem=0
        wishitem=0
        if request.user.is_authenticated:
         totalitem = len(Cart.objects.filter(user=request.user))
         totalitem = len(Wishlist.objects.filter(user=request.user))
         wishlist_items = Wishlist.objects.filter(Q(product=product) & Q(user=request.user))
         
        return render(request,"app/productdetail.html",locals())

class CustomerRegistration(View):
    def get(self, request):
        form = CustomerRegistrationForm()
        totalitem=0
        wishitem=0
        if request.user.is_authenticated:
         totalitem = len(Cart.objects.filter(user=request.user))
         totalitem = len(Wishlist.objects.filter(user=request.user))
        return render(request, 'app/customerregistration.html', {'form': form})

    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Congratulations! User registered successfully.")
            return render(request, 'app/customerregistration.html', {'form': CustomerRegistrationForm()})  # Reset form on success
        else:
            messages.error(request, "Invalid input data.")

@method_decorator(login_required,name='dispatch')
class ProfileView(View):
    def get(self, request):
        form = CustomerProfileForm()
        totalitem=0
        wishitem=0
        if request.user.is_authenticated:
         totalitem = len(Cart.objects.filter(user=request.user))
         totalitem = len(Wishlist.objects.filter(user=request.user))
        return render(request, 'app/profile.html', locals())

    def post(self, request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            user=request.user
            name=form.cleaned_data['name']
            locality=form.cleaned_data['locality']
            city=form.cleaned_data['city']
            mobile=form.cleaned_data['mobile']
            state=form.cleaned_data['state']
            zipcode=form.cleaned_data['zipcode']
            reg=Customer(user=user,name=name,locality=locality,mobile=mobile,city=city,state=state,zipcode=zipcode)
            reg.save()
            messages.success(request,"congratulation! Profile save Successfully")
        else:
            messages.warning(request,"Invalid Input Data")
        return render(request, 'app/profile.html', locals())
  
def address(request):
    add=Customer.objects.filter(user=request.user)
    totalitem=0
    wishitem=0
    if request.user.is_authenticated:
         totalitem = len(Cart.objects.filter(user=request.user))
         totalitem = len(Wishlist.objects.filter(user=request.user))
    return render(request,'app/address.html',locals())


class updateAddress(View):
    def get(self, request, pk):
        add = get_object_or_404(Customer, pk=pk)
        form = CustomerProfileForm(instance=add)

        total_cart_items = Cart.objects.filter(user=request.user).count()
        total_wishlist_items = Wishlist.objects.filter(user=request.user).count()

        return render(request, 'app/updateAddress.html', {
            'form': form,
            'add': add,
            'total_cart_items': total_cart_items,
            'total_wishlist_items': total_wishlist_items,
        })

    def post(self, request, pk):
        add = get_object_or_404(Customer, pk=pk)
        form = CustomerProfileForm(request.POST, instance=add)

        if form.is_valid():
            form.save()
            messages.success(request, "Congratulations! Profile saved successfully.")
            return render(request, 'app/updateAddress.html', {'form': form, 'add': add})

        messages.warning(request, "Invalid input data.")
        return render(request, 'app/updateAddress.html', {'form': form, 'add': add})

@login_required
def add_to_cart(request):
    user = request.user
    product_id = request.GET.get('prod_id')
    product = Product.objects.get(id=product_id)
    Cart(user=user, product=product).save()  # Ensure you call the save method with parentheses
    return redirect("/cart")
@login_required
def show_cart(request):
    user = request.user
    cart = Cart.objects.filter(user=user)  # Corrected to Cart.objects.filter
    amount=0
    for p in cart:
        value=p.quantity*p.product.discounted_price
        amount=amount+value
    totalamount=amount+40
    totalitem=0
    wishitem=0
    if request.user.is_authenticated:
         totalitem = len(Cart.objects.filter(user=request.user))

    return render(request, 'app/addtocart.html', locals())

@method_decorator(login_required,name='dispatch')
class checkout(View):
    def get(self,request):
        totalitem=0
        totalitem = len(Wishlist.objects.filter(user=request.user))
        if request.user.is_authenticated:
         totalitem = len(Cart.objects.filter(user=request.user))
        user=request.user
        add=Customer.objects.filter(user=user)
        cart_items=Cart.objects.filter(user=user)
        famount=0
        for p in cart_items:
            value=p.quantity*p.product.discounted_price
            famount=famount+value
            totalamount=famount+40
        return render(request, 'app/checkout.html', locals())
    
@login_required
def orders(request):
    totalitem=0
    wishitem=0
    if request.user.is_authenticated:
         totalitem = len(Cart.objects.filter(user=request.user))
         totalitem = len(Wishlist.objects.filter(user=request.user))
    order_placed = OrderPlaced.objects.filter(user=request.user)
    return render(request, 'app/orders.html', locals())


def plus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = get_object_or_404(Cart, Q(product=prod_id) & Q(user=request.user))
        c.quantity += 1
        c.save()

        user = request.user
        cart = Cart.objects.filter(user=user)

        amount = sum(p.product.discounted_price * p.quantity for p in cart)
        totalamount = amount + 40  # Assuming 40 is a fixed shipping fee

        data = {
            'quantity': c.quantity,
            'amount': amount,
            'totalamount': totalamount,
        }

        return JsonResponse(data)

def minus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = get_object_or_404(Cart, Q(product=prod_id) & Q(user=request.user))
        
        if c.quantity > 1:
            c.quantity -= 1
            c.save()
        else:
            c.delete()  # Remove the item if quantity is 1

        user = request.user
        cart = Cart.objects.filter(user=user)

        amount = sum(p.product.discounted_price * p.quantity for p in cart)
        totalamount = amount + 40

        data = {
            'quantity': c.quantity if c.quantity > 0 else 0,  # Return 0 if deleted
            'amount': amount,
            'totalamount': totalamount,
        }

        return JsonResponse(data)

def remove_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = get_object_or_404(Cart, Q(product=prod_id) & Q(user=request.user))
        c.delete()  # Remove the item from the cart

        user = request.user
        cart = Cart.objects.filter(user=user)

        amount = sum(p.product.discounted_price * p.quantity for p in cart)
        totalamount = amount + 40

        data = {
            'quantity': 0,  # Since the item was removed
            'amount': amount,
            'totalamount': totalamount,
        }

        return JsonResponse(data)
    
@login_required
def show_Wishlist(request):
    user=request.user
    totalitem=0
    wishitem=0
    totalitem=len(Cart.objects.filter(user=request.user))
    totalitem = len(Wishlist.objects.filter(user=request.user))
    return render(request,"app/wishlist.html",locals())

def plus_Wishlist(request):
    if request.method == 'GET':
        if not request.user.is_authenticated:
            return JsonResponse({'message': 'User not authenticated'}, status=403)

        prod_id = request.GET.get('prod_id')
        product = get_object_or_404(Product, id=prod_id)
        user = request.user

        # Add product to wishlist
        Wishlist.objects.get_or_create(user=user, product=product)
        
        data = {
            'message': 'Wishlist Added Successfully',
        }
        return JsonResponse(data)

def minus_Wishlist(request):
    if request.method == 'GET':
        if not request.user.is_authenticated:
            return JsonResponse({'message': 'User not authenticated'}, status=403)

        prod_id = request.GET.get('prod_id')
        product = get_object_or_404(Product, id=prod_id)
        user = request.user

        # Remove product from wishlist
        Wishlist.objects.filter(user=user, product=product).delete()
        
        total_items = Wishlist.objects.filter(user=user).count()
        
        data = {
            'message': 'Wishlist removed successfully',
            'total_items': total_items,
        }
        return JsonResponse(data)
    
@login_required  
def search(request):
    query = request.GET.get('search')
    products = Product.objects.filter(title__icontains=query)  # Adjust according to your field
    totalitem = 0
    
    if request.user.is_authenticated:
        totalitem = Wishlist.objects.filter(user=request.user).count()  # Correctly get the count

    return render(request, 'app/search.html', {'products': products, 'totalitem': totalitem})

