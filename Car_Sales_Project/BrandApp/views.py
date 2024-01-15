from django.shortcuts import get_object_or_404,render,redirect
from django.views.generic import CreateView,DetailView
from django.urls import reverse_lazy
from . models import BrandModel
from . forms import BranModelForm 
from CarApp.models import CarModel 
from django import forms 
from CommentsApp.forms import CommentForm  
from CommentsApp.models import Order
# Create your views here.
class BrandModelView(CreateView):
    model = BrandModel 
    form_class = BranModelForm 
    template_name = 'add_brand.html' 
    context_object_name = 'form' 
    success_url = reverse_lazy('brand_details')

class DetailsCarView(DetailView):
    model = CarModel 
    pk_url_kwarg = 'id'
    template_name = 'car_details.html' 
    context_object_name = 'data'

    def post (self, request, *args, **kwargs):
        comment_form = CommentForm(data=self.request.POST)
        car = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.cars = car
            new_comment.save()
        return self.get(request, *args, **kwargs) 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object 
        comments = post.comments.all()
        comment_form = CommentForm()
        
        context['comments'] = comments
        context['comment_form'] = comment_form
        return context 

def buy_button_view(request, id):
    obj = get_object_or_404(CarModel, pk=id)

    if request.method == 'POST':
        Order.objects.create(car =obj, customer = request.user) 
        
        quantity_to_decrease = request.POST.get('quantity_to_decrease', 1)

        obj.quantity -= int(quantity_to_decrease)
        obj.save()
    return redirect('order_history') 

def Order_history(request):
    orders = Order.objects.filter(customer = request.user).order_by('order_date') 
    return render(request, 'place_order_history.html', {'orders': orders})
