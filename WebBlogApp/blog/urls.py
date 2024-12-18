from . import views
from django.urls import path
from django.contrib import admin

urlpatterns=[
    path('admin/', admin.site.urls),
    path('<slug:slug>/',views.BlogView.as_view(),name='blog_view'),
    path('about',views.AboutView.as_view(),name='about_view'),              #path('',views.HomeView.as_view(),name='home_view')
    path('',views.PostList.as_view(),name='home')
]

#example.com/dogs

