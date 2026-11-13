
# from django.shortcuts import render, redirect
# from .models import book
# Create your views here.



# def home(request):
#   data={"name":"hashmi","age":20,"place":"kdr","hobbies":["foodball,cricket,volleyball"]}

#   return render(request,"myapp/home.html",data)



from django.shortcuts import render
from django.http import HttpResponse
from .models import book
from. forms import book_form
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate

# Create your views here.

def home(request):
    a=book.objects.all()
    return render(request,'myapp/home2.html',{'a':a})

from .models import book

def add(request):
    if request.method == "POST":
        b = book()
        b.title = request.POST.get('t')
        b.author = request.POST.get('a')
        b.price = request.POST.get('p')
        b.pdf = request.FILES.get('f')
        b.cover = request.FILES.get('c')

        b.save()

        return home(request)

    return render(request, 'myapp/add.html')

def add_form(request):
    if request.method=="POST":
        form=book_form(request.POST)
        if form.is_valid():
            form.save()
            return home(request)
    form=book_form()
    return render(request,"myapp/add_form.html",{'form':form})

def register(request):
    if request.method == "POST":
        u = request.POST['u']
        e = request.POST['e']
        f = request.POST['f']
        l = request.POST['l']
        p = request.POST['p']
        cp = request.POST['cp']

        if p == cp:
            user = User.objects.create_user(
                username=u,
                email=e,
                first_name=f,
                last_name=l,
                password=p
            )

            return home(request)

        else:
            return HttpResponse("Passwords Don't Match")

    return render(request, "myapp/signup.html")

def user_login(request):
    if request.method=="POST":
        u=request.POST['u']
        p=request.POST['p']
        user=authenticate(username=u,password=p)
        if user:
            login(request,user)
            return home(request)
        else:
            return HttpResponse("Invalid Credentials")
    return render(request,"myapp/login.html")


def order_success(request):
    return render(request, "myapp/order_success.html")

def order(request):
    return render(request, "myapp/order.html")
def home(request):
    a = book.objects.all()
    return render(request, 'myapp/home2.html', {'a': a})



