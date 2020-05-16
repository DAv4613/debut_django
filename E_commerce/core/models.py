from django.db import models
from django.conf import settings
from django.shortcuts import reverse


CATEGORY_CHOICES = (
   ( 'bb', 'boubou'),
   ( 'rb', 'robe'),
   ( 'jp', 'jupe'),
   ( 'pt', 'pantalon'),
   ( 'mi', 'miel'),
   ( 'be', 'beurre'),
   ( 'ba', 'basin'),
   ( 'pagne baoule', 'pagne baoule')
)
LABEL_CHOICES = (
   ( 'p', 'primary'),
   ( 'd', 'danger'),
   ( 'w', 'warning'),
   ( 'b', 'blue'),   
)
class Over_product(models.Model):
    title = models.CharField(max_length=200,  blank=True, null=True)
    slug = models.SlugField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='images/')
    label = models.CharField(choices=LABEL_CHOICES, max_length=30,blank=True, null=True )

    def __str__(self):
        return self.title

class Slide(models.Model):
    title = models.CharField(max_length=200,  blank=True, null=True)
    description = models.TextField( blank=True, null=True)
    slug = models.SlugField()
    image = models.ImageField(upload_to='images/')
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=30,blank=True, null=True )

    def __str__(self):
        return self.title
      

class Item(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    description = models.TextField( )
    reduction = models.IntegerField()
    price = models.IntegerField()
    discount_price = models.IntegerField(blank=True, null=True)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=30,blank=True, null=True )
    label = models.CharField(choices=LABEL_CHOICES, max_length=1, blank=True, null=True )
    image = models.ImageField(upload_to='images/')
      

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("core:produits", kwargs={
            'slug': self.slug
        })

    def get_add_to_cart_url(self):
        return reverse("core:add-to-cart", kwargs={
            'slug': self.slug
        })
    
    def get_remove_from_cart_url(self):
        return reverse("core:remove-from-cart", kwargs={
            'slug': self.slug
        })
    
    def get_add_to_cart_home_page(self):
        return reverse("core:add-to-cart-home-page", kwargs={
            'slug': self.slug
        })

    
    

class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.item.title}"

    def get_total_item_price(self):
        return self.quantity * self.item.price
    
    def get_total_item_discount_price(self):
        return self.quantity * self.item.discount_price
    
   
    def get_final_price(self):
        if self.item.price:
            return self.get_total_item_price()
        return self.get_total_item_discount_price()


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
    
    def get_total(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_final_price()
        return total 
