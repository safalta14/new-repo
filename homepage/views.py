from django.shortcuts import render
from.models import News,Category
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from.forms import Newsform

# Create your views here.
def home(request):
    dist = {
        'news':News.objects.all(),
        'category':Category.objects.all(),
        'profession':'Actor',
        'address':'address',
        'age':60,
     }
    return render(request,  "index.html",dist)

def about(request):
    return render(request, "about.html")
#DELETE NEWS
def deleteNews(request,id):
    news=News.objects.get(id=id)
    news.delete()
    messages.success(request,"successfully deleted")
    return HttpResponseRedirect(reverse('homepage:dashboard'))

def addnews(request):
    form =Newsform
    dist= {
        'forms':form
    }
    if request.method =='POST':
        form=Newsform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"successfully added news")
            return HttpResponseRedirect(reverse('homepage:dashboard'))
    return render(request,"news.html",dist)

def news_detail(request,id):
    print(id)
    data=News.objects.get(id=id)
    return render(request,"news_detail.html",{'data':data})


count=0

#logout function
def logoutpage(request):
    logout(request)
    messages.success(request,'successfully logout')
    return HttpResponseRedirect(reverse('homepage:loginpage'))


def loginpage(request):
    global count
    if request.method=='POST':
        username = request.POST['email']
        password = request.POST['password']
        user=None
        if count>=3:
            messages.error(request,"you cant login more than 3 times")
        else:
             user=authenticate(request,username =username,password=password)
        if user:
            login(request, user)
            messages.success(request,"successfully log in")
            return  HttpResponseRedirect(reverse('homepage:dashboard'))
        
        else:
            count+=1
            if count>=3:
                messages.success(request,"you cannot log in more than 3 times")
            messages.error(request,"incorrect unsername or password")
            pass

    return render(request, "login.html")

def dashboard(request):
    news=News.objects.all().count()
    category=Category.objects.all().count
    dist={
        'news_count':news,
        'category_count':category
    }

    return render(request,"dashboard.html",dist)


 

    