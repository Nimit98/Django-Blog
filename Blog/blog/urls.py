from . import views
from django.urls import path

app_name = 'blog'

urlpatterns = [
    path('register/',views.register,name='register'),
    path('detail/<int:pk>/',views.BlogDetailView.as_view(),name='blog_detail'),
    path('login/',views.user_login,name='login'),
    path('logout/',views.user_logout,name='logout'),
    path('profile/',views.profile,name='profile'),
    path('create-blog/',views.createBlog,name='createBlog'),
    path('comment/<int:pk>/',views.comment,name='comment'),
]