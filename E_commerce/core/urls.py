from django.urls import path, include
from django.conf.urls import url 
from .views import ( OrderSammaryView, ItemDetailView)

from . import views

app_name = 'core'
urlpatterns = [
  
    path('', views.item_list, name='item_list'),
    path('connexion', views.connexion, name='connexion'),
    #url(r'Articles/(?P<id>[0-9]+)$',views.details, name='produits'),
    #path('search/', views.search, name='search'),
    #path('', HomeView.as_view(), name='home'),
    path('produits/<slug>/', ItemDetailView.as_view(), name='produits'),
    path('commande', OrderSammaryView.as_view(), name='commande'),
    path('add-to-cart/<slug>/', views.add_to_cart, name="add-to-cart"),
    path('remove-from-cart/<slug>/', views.remove_from_cart, name="remove-from-cart"),
    path('add-to-cart-home-page/<slug>/', views.add_to_cart_home_page, name="add-to-cart-home-page"),
    path('remove-single-from-cart/<slug>/', views.remove_single_from_cart, name="remove-single-from-cart"),
    
   
]