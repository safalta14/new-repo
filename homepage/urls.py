from django.urls import path
from.views import home, about
from.views import home,news_detail,loginpage,dashboard,logoutpage,addnews,deleteNews

app_name='homepage'

urlpatterns=[
    path("", home, name='home'),
    path("about",about,name='about'),
    path('news_detail/<int:id>', news_detail,name="news_detail"),
    path("login",loginpage,name='loginpage'),
    path('logout',logoutpage,name='logoutpage'),

    #dashboard
    path('dashboard',dashboard, name='dashboard'),
    path('addnews',addnews, name='addnews'),
    path('delete-news/<int:id>',deleteNews, name='deleteNews')

]