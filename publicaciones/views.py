from django.shortcuts import render
from .models import BlogPost
from django.views.generic import ListView, DetailView
from django.views.generic import TemplateView

# Create your views here.
class PostListView(ListView):
    model = BlogPost
    context_object_name = 'blogposts'
    template_name = 'post/lista_post.html'

    def get_queryset(self):
        return BlogPost.objects.all()

class PostDetalleView(DetailView):
    model = BlogPost
    context_object_name = "blogposts"
    template_name = 'post/detalles_post.html'

class HomeView(TemplateView):
    template_name = 'post/home.html'

class AboutMeView(TemplateView):
    template_name = 'post/acerca_de_mi.html'