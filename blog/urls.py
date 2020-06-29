from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),

    path('signup/', views.signup, name='register'),

    path('login/', auth_views.LoginView.as_view(
        template_name='blog/login.html'), name='login'),

    path('logout', auth_views.LogoutView.as_view(
        template_name='blog/loggedout.html'), name='logout'),

    path('create_post/', views.createPost, name='create_post'),

    path('posts/<str:title>/', views.post_details, name='post_details'),

    path('myposts/', views.myposts, name='my_posts'),

    path('comment/<int:id>/', views.add_comment, name='add_comments'),

    path('delete_post/<int:id>', views.delete_post, name='delete_post'),

    path('delete/<int:id>/', views.delete_comment, name='delete_comment'),
]
