from django.contrib import admin

from .models import Item, OrderItem, Order, Slide, Over_product

class ItemAdmin(admin.ModelAdmin):
    fields = ('title', 'slug', 'reduction', 'label', 'description', 'price', 'discount_price', 'category','image')
    prepopulated_fields = {'slug':('title', ),}

class SlideAdmin(admin.ModelAdmin):
    fields = ('title', 'slug', 'description', 'category','image')
    prepopulated_fields = {'slug':('title', ),}

class Over_productAdmin(admin.ModelAdmin):
    fields = ('title', 'slug', 'price','label','image')
    prepopulated_fields = {'slug':('title', ),}

    

admin.site.register(Over_product, Over_productAdmin)
admin.site.register(Slide, SlideAdmin)
admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(Item, ItemAdmin)

