# from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .forms import ProductForm
from .models import Product

# Create your views here.

class ProductDeleteView(View):
    template_name = "product/product_delete.html"
    def get_object(self):
        id = self.kwargs.get('id')
        obj = None
        if id is not None:
            obj = get_object_or_404(Product, id=id)
        return obj

    def get(self, request, id=None, *args, **kwargs):
        context = {}
        obj = self.get_object()
        if object is not None:
            context['object'] = obj
        return render(request, self.template_name, context)

    def post(self, request, id=None, *args, **kwargs):
        context = {}
        obj = self.get_object()
        if object is not None:
            obj.delete()
            context['object'] = None
            redirect('products../../')
        return render(request, self.template_name, context)

class ProductUpdateView(View):
    template_name = "product/product_update.html"
    def get_object(self):
        id = self.kwargs.get('id')
        obj = None
        if id is not None:
            obj = get_object_or_404(Product, id=id)
        return obj

    def get(self, request, id=None, *args, **kwargs):
        context = {}
        obj = self.get_object()
        if object is not None:
            form = ProductForm(instance=obj)
            context['object'] = obj
            context['form'] = form
        return render(request, self.template_name, context)

    def post(self, request, id=None, *args, **kwargs):
        context = {}
        obj = self.get_object()
        if object is not None:
            form = ProductForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
            context['object'] = obj
            context['form'] = form
        return render(request, self.template_name, context)

class ProductCreateView(View):
    template_name = "product/create.html"
    def get(self, request, *args, **kwargs):
        form = ProductForm()
        context = {"form": form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            form = ProductForm()
        context = {"form": form}
        return render(request, self.template_name, context)

class ProductListView(View):
    template_name = "product/product_list.html"
    queryset = Product.objects.all()
    def get(self, request, id=None, *args, **kwargs):
        context = {'object_list': self.queryset}
        return render(request, self.template_name, context)

class HomeView(View):
    template_name = "product/home.html"
    def get(self, request, id=None, *args, **kwargs):
        context = {}
        if id is not None:
            obj = get_object_or_404(Product, id=id)
            context['object'] = obj
        return render(request, self.template_name, context)


def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})

def about_view(request, *args, **kwargs):
    return render(request, "about.html", {})

def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})


def product_create_view(request):
    initial_data = {
        "title": "This is my awesome title",
    }
    form = ProductForm(request.POST or None, initial=initial_data)
    if form.is_valid():
        form.save()
        form = ProductForm()

    context = {
        "form": form
    }
    # return HttpResponse("<h1>Hello World</h1>")
    return render(request, "product/create.html", context)

def product_search_view(request, id):
    obj = get_object_or_404(Product, id=id)
    # obj = Product.objects.get(id=id)
    context = {
        "object": obj
    }
    # return HttpResponse("<h1>Hello World</h1>")
    return render(request, "product/detail.html", context)

def product_detail_view(request):
    obj = Product.objects.get(id=1)
    context = {
        "object": obj
    }
    # return HttpResponse("<h1>Hello World</h1>")
    return render(request, "product/detail.html", context)

def product_delete_view(request, id):
    obj = get_object_or_404(Product, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('../../')
    context = {
        "object": obj
    }
    return render(request, "product/product_delete.html", context)


def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        "object_list": queryset

    }
    return render(request,"product\product_list.html", context)

