from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name="home"),
    path('post/', views.PostListView.as_view(), name="lista_post"),
    path('detail/<int:pk>', views.PostDetalleView.as_view(), name="detalles_post"),
    path('platform_posts/', views.PostListView.as_view(template_name='post/plataforma.html'), name='plataforma_posts'), 
    path('youtube_posts/', views.PostListView.as_view(template_name='post/youtube.html'), name='youtube_posts'), 
    path('about_me', views.AboutMeView.as_view(), name="about_me"),
]