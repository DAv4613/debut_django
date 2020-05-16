from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView,ListView,View
from django.utils import timezone
from django.db.models import Q
from .models import Item, Order, OrderItem, Slide, Over_product
from django.contrib.auth.models import User
from .forms import UserForm

# Create your views here.
# def search(request):
    
#     if request.method =='GET':
#         srch = request.GET[('srh')]
#         if srch:
#             match = Item.objects.filter(title__icontains=srch)
#             if match:
#                 return render(request, 'index.html', {'sr':match})
#             else:
#                 messages.error(request, 'Aucun article disponible')
#         else:
#             return redirect('index.html')
#     return render(request, 'index.html')
def connexion(request):
    if request.method=='POST':
        form1 = UserForm(request.POST)
        if form1.is_valid():
            username = form1.cleaned_data['username']
            email = form1.cleaned_data['email']
            first_name = form1.cleaned_data['first_name']
            last_name = form1.cleaned_data['last_name']
            password = form1.cleaned_data['username']
            User.objects.create_user(username=username, email=email, first_name=first_name, last_name = last_name, password=password)
        return HttpResponseRedirect( "item_list")
    else:
        form1= UserForm()
    return render(request, "connexion.html", {'form1':form1})


def item_list(request):
    items = Item.objects.filter()
    slides = Slide.objects.filter()
    cat = Over_product.objects.filter()
    return render(request, 'index.html', context={'items':items, 'slides':slides, 'cat':cat})

#def produits(request, id):
#    article = get_object_or_404(Item, pk=id)
#    return render(request, 'produits.html', {'Article':article})

def connexion(request):
    if request.method=='POST':
        username= request.POST['username']
        password= request.POST['password']

        user.authenticate(request, username=username, password=password)
        if user is not None:
            connexion(request, user)
            return redirect('/')
        else:
            contex = {'msg': 'mot de passe ou id incorrect'}

class HomeView(ListView):
    model = Item
    template_name = 'index.html'

class ItemDetailView(DetailView):
   model = Item
   template_name = 'produits.html'

#def details(request, id):
#    article = Item.objects.get(pk=id)
#    return render(request, 'core/produits.html', {'article': article})


class OrderSammaryView(LoginRequiredMixin,View):
    def get(self, *args, **kwargs):
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            context = {
                'object': order
            }
            return render(self.request, 'commande.html',context )
        except ObjectDoesNotExist:
            messages.error(self.request, "Votre panier est vide ")
            return redirect("/")
        
    
@login_required
def add_to_cart(request, slug):
    
    item = get_object_or_404(Item, slug=slug)
    order_item, created = OrderItem.objects.get_or_create(
        item=item, 
        user=request.user, 
        ordered= False)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, "La quantité a été modifié avec success")
            return redirect("core:commande")
        else:
            order.items.add(order_item)
            messages.info(request, "L'article a été ajouter avec succes")
            return redirect("core:commande")
    else:
        ordered_date = timezone.now()
        order= Order.objects.create(user = request.user, ordered_date=ordered_date)
        order.items.add(order_item)
        messages.info(request, "L'article a été ajouter dans votre panier")
    return redirect("core:commande")

@login_required
def add_to_cart_home_page(request, slug):
    
    item = get_object_or_404(Item, slug=slug)
    order_item, created = OrderItem.objects.get_or_create(
        item=item, 
        user=request.user, 
        ordered= False)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
            #messages.info(request, "La quantité a été modifié avec success")
            return redirect("core:home")
        else:
            order.items.add(order_item)
            #messages.info(request, "L'article a été ajouter avec succes")
            return redirect("core:home")
    else:
        ordered_date = timezone.now()
        order= Order.objects.create(user = request.user, ordered_date=ordered_date)
        order.items.add(order_item)
        #messages.info(request, "L'article a été ajouter dans votre panier")
    return redirect("core:home")

@login_required
def remove_from_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user = request.user,
                ordered = False
            )[0]
            order.items.remove(order_item)
            messages.info(request, "L'article a été supprimé dans votre panier  ")
        else:
            messages.info(request, "cet articles n'est plus dans votre panier")
            return redirect("core:commande")
    else:
        messages.info(request, "Aucun article dans votre panier")    
        return redirect("core:commande")
    return redirect("core:commande")

@login_required
def remove_single_from_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user = request.user,
                ordered = False
            )[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
            else:   
                order.items.remove(order_item)
            
            return redirect("core:commande")
        else:
            messages.info(request, "cet articles n'est plus dans votre panier")
            return redirect("core:produits", slug = slug)
    else:
        messages.info(request, "Aucun article dans votre panier")    
        return redirect("core:produits", slug = slug)
    return redirect("core:produits", slug = slug)
