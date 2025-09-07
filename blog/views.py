from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
# from django.urls import reverse
from .forms import ArticleForm
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Article


# Create your views here.

def article_delete_view(request, id):
    obj = get_object_or_404(Article, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('../../')
    context = {
        "object": obj
    }
    return render(request, "blog/article_delete.html", context)

class ArticleDeleteView(View):
    template_name = "blog/article_delete.html"
    def get_object(self):
        id = self.kwargs.get('id')
        obj = None
        if id is not None:
            obj = get_object_or_404(Article, id=id)
        return obj

    def get(self, request, *args, **kwargs):
        context = {}
        obj = self.get_object()
        if object is not None:
            context['object'] = obj
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        context = {}
        obj = self.get_object()
        if object is not None:
            obj.delete()
            context['object'] = None
            redirect('../../')
        return render(request, self.template_name, context)

class HomeView(View):
    def get(request, *args, **kwargs):
        return render(request, "home.html", {})


class ArticleListView(ListView):
    template_name = "blog/article_list.html"
    queryset = Article.objects.all()

class ArticleCreateView(CreateView):
    template_name = "blog/artcle_create.html"
    form_class = ArticleForm
    queryset = Article.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class ArticleDetailView(DetailView):
    template_name = "blog/article_detail.html"
    # queryset = Article.objects.all()

    def get_object(self):
        id_=self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)

class ArticleUpdateView(UpdateView):
    template_name = "blog/artcle_create.html"
    form_class = ArticleForm
    queryset = Article.objects.all()

    def get_object(self):
        id_=self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

# class ArticleDeleteView(DeleteView):
#     template_name = "blog/article_delete.html"
#     # queryset = Article.objects.all()
#
#     def get_object(self):
#         id_=self.kwargs.get("id")
#         return get_object_or_404(Article, id=id_)

    # def get_success_url(self):
    #     return reverse("blog: article-list")


# def article_detail_view(request):
#     obj = Article.objects.get(id=1)
#     context = {
#         'object': obj
#     }
#     return render(request, "blog/article_detail.html", context)

# def article_list_view(request):
#     query_set = Article.objects.all()
#     context = {
#         "article_list": query_set
#     }
#     return render(request, "blog/article_list.html", context)

# def article_search_view(request, id):
#     obj = get_object_or_404(Article, id=id)
#     # obj = Product.objects.get(id=id)
#     context = {
#         "object": obj
#     }
#     # return HttpResponse("<h1>Hello World</h1>")
#     return render(request, "blog/article_detail.html", context)