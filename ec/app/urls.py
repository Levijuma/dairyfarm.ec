from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views  
from .forms import LoginForm, MyPasswordResetForm, PasswordChangeForm, MysetPasswordForm
from django.contrib import admin

urlpatterns = [
    # Home and static pages
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),  
    path('contact/', views.contact, name='contact'),  
    
    # Category and product views
    path('category/<slug:val>/', views.CategoryView.as_view(), name='category'),
    path('category-title/<val>/', views.CategoryTitle.as_view(), name='category-title'),  
    path('product-detail/<int:pk>/', views.ProductDetail.as_view(), name='product-detail'),
    
    # Profile and address views
    path('profile/', views.ProfileView.as_view(), name='profile'),  
     path('address/', views.address, name='address'), # Ensure this function is defined in views
    path('updateAddress/<int:pk>/', views.updateAddress.as_view(), name='updateAddress'),
    path('addto-cart/', views.add_to_cart, name='add_to_cart'),
    path('cart/',views.show_cart,name='showcart'),
    path('checkout/',views.checkout.as_view(),name='checkout'),
     path('orders/', views.orders,name='orders'),
     path('search/', views.search,name='search'),

    path('pluscart/', views.plus_cart),
    path('minuscart/', views.minus_cart),
    path('removecart/', views.remove_cart),
    path('pluswishlist/', views.plus_Wishlist),
    path('minuswishlist/', views.minus_Wishlist),

    
    # User authentication
    path('registration/', views.CustomerRegistration.as_view(), name='customerregistration'),
    path('accounts/login/', auth_views.LoginView.as_view(
        template_name='app/login.html', 
        authentication_form=LoginForm
    ), name='login'),

    path('password-reset/', auth_views.PasswordResetView.as_view(
        template_name='app/password_reset.html', 
        form_class=MyPasswordResetForm,
    ), name='password_reset'),

    path('passwordchange/', auth_views.PasswordChangeView.as_view(
        template_name='app/changepassword.html', 
        form_class=PasswordChangeForm,
        success_url='/passwordchangedone/'  # Optionally use reverse_lazy
    ), name='passwordchange'),

    path('passwordchangedone/', auth_views.PasswordChangeDoneView.as_view(
        template_name='app/passwordchangedone.html', 
    ), name='passwordchangedone'),

   path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
  


    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='app/password_reset_done.html', 
    ), name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='app/password_reset_confirm.html',  
        form_class=MysetPasswordForm
    ), name='password_reset_confirm'),

    path('reset-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='app/password_reset_complete.html',  
    ), name='password_reset_complete'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
admin.site.site_header="Neel  Dairy"
admin.site.site_title="Neel  Dairy"
admin.site.site_index_title =" welcomre to Neel  Dairy shop"