from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('home/', views.home, name='home'),
    path('add/', views.add_product, name='add_product'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('delete<int:product_id>',
         views.delete_product, name='delete_product')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
