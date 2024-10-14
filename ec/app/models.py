from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


STATE_CHOICES = [
        ('001', 'Mombasa'),
        ('002', 'Kwale'),
        ('003', 'Kilifi'),
        ('004', 'Tana River'),
        ('005', 'Lamu'),
        ('006', 'Taita-Taveta'),
        ('007', 'Garissa'),
        ('008', 'Wajir'),
        ('009', 'Mandera'),
        ('010', 'Marsabit'),
        ('011', 'Isiolo'),
        ('012', 'Meru'),
        ('013', 'Tharaka-Nithi'),
        ('014', 'Embu'),
        ('015', 'Kitui'),
        ('016', 'Machakos'),
        ('017', 'Makueni'),
        ('018', 'Nyandarua'),
        ('019', 'Nyeri'),
        ('020', 'Kirinyaga'),
        ('021', 'Murang’a'),
        ('022', 'Kiambu'),
        ('023', 'Turkana'),
        ('024', 'West Pokot'),
        ('025', 'Samburu'),
        ('026', 'Trans-Nzoia'),
        ('027', 'Uasin Gishu'),
        ('028', 'Elgeyo-Marakwet'),
        ('029', 'Nandi'),
        ('030', 'Baringo'),
        ('031', 'Laikipia'),
        ('032', 'Nakuru'),
        ('033', 'Narok'),
        ('034', 'Kajiado'),
        ('035', 'Kericho'),
        ('036', 'Bomet'),
        ('037', 'Kakamega'),
        ('038', 'Vihiga'),
        ('039', 'Bungoma'),
        ('040', 'Busia'),
        ('041', 'Siaya'),
        ('042', 'Kisumu'),
        ('043', 'Homa Bay'),
        ('044', 'Migori'),
        ('045', 'Kisii'),
        ('046', 'Nyamira'),
        ('047', 'Nairobi'),
    ]


CATEGORY_CHOICES = (
    ('CR', 'Curd'),
    ('ML', 'Milk'),  
    ('LS', 'Lassi'),
    ('MS', 'Milkshake'),
    ('PN', 'Paneer'),  
    ('GH', 'Ghee'),
    ('CZ', 'Cheese'),
    ('IC', 'Ice-Creams'),
)

class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    composition = models.TextField(default='')
    proapp = models.TextField(default='')
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)  
    product_image = models.ImageField(upload_to='product')

    def __str__(self):
        return self.title


class Customer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    mobile = models.IntegerField(default=0)
    zipcode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICES, max_length=100)  


    def __str__(self):
        return self.name
    
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
    quantity=models.PositiveIntegerField(default=1)
    
    @property
    def total_cost(self):
        return self.quantity *self.product.discounted_price
    

STATUS_CHOICE = (
    ('Accepted', 'Accepted'),
    ('Packed', 'Packed'),
    ('On The Way', 'On The Way'),
    ('Delivered', 'Delivered'),
    ('Cancel', 'Cancel'),
    ('Pending', 'Pending'),
)

    
class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.FloatField()
    razorpay_order_id = models.CharField(max_length=100, blank=True, null=True)  # Ensure this is defined
    razorpay_payment_status = models.CharField(max_length=100, blank=True, null=True)
    paid = models.BooleanField(default=False)
    

class OrderPlaced(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    Product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField(default=1)
    ordered_data = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50,choices=STATE_CHOICES,default='pending')
    payment=models.ForeignKey(Payment,on_delete=models.CASCADE,default="")
    
    @property
    def total_cost(self):
        return self.quantity*self.product.discounted_price
    

class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Corrected 'use' to 'user' and 'on_delete_dlete' to 'on_delete'
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

class Contact(models.Model):
    names = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=13)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.names} - {self.email}"
