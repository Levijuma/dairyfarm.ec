from django.contrib import admin
from .models import Cart,Product, Customer,Payment,OrderPlaced,Wishlist,Contact
from django.shortcuts import render
from django.utils.html import format_html
from django.urls import reverse
from django.contrib.auth.models import Group
# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'discounted_price', 'selling_price', 'category', 'product_image')  # Display these fields in the list view
    search_fields = ('title', 'category__name')  # Add search capability (assuming 'category' has a 'name' field)

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_user', 'locality', 'city', 'state', 'zipcode')  # Updated 'user' to 'get_user'
    search_fields = ('user__username', 'locality', 'city') 
     

    # Define a method to show the user's name if it's a foreign key
    def get_user(self, obj):
        return obj.user.username  # Assuming 'user' is a ForeignKey to the User model

    get_user.short_description = 'User'

@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'product', 'quantity']  
def products(self, obj):
    link = reverse("admin:app_product_change", args=[obj.product.pk])
    return format_html('<a href="{}">{}</a>', link, obj.product.title)
 
@admin.register(Payment)
class PaymentModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'amount', 'razorpay_order_id', 'razorpay_payment_status', 'paid']

@admin.register(OrderPlaced)
class OrderPlacedModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'name', 'Product', 'quantity', 'ordered_data', 'status', 'payment']
def customers(self, obj):
        link = reverse("admin:app_customer_change", args=[obj.product.pk])
        return format_html('<a href="{}">{}</a>', link, obj.product.title)

def products(self, obj):
        link = reverse("admin:app_product_change", args=[obj.product.pk])
        return format_html('<a href="{}">{}</a>', link, obj.product.title)
    
    
@admin.register(Wishlist)
class WishlistModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'product_link']

    def product_link(self, obj):
        link = reverse("admin:app_product_change", args=[obj.product.pk])
        return format_html('<a href="{}">{}</a>', link, obj.product.title)

      
    
    product_link.short_description = 'Product'  # Optional: to change the column name in admin
    
admin.site.unregister(Group)
admin.site.register(Contact)