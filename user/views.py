from django.shortcuts import render,redirect,HttpResponse
from .models import Menu
from .forms import*
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login #i have login keyword for views also so that why i hev change this
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(req):
    menu = Menu.objects.all()
    return render(req, 'home.html',{'menu':menu})

def menu(req):
    menu = Menu.objects.all()
    return render(req, 'menu.html',{'menu':menu})


def about(req):
    return render(req, 'about.html')


def contact(req):
    return render(req, 'contact.html')

def bookseat(req):
    return render(req, 'bookseat.html')




@login_required(login_url='login/')
def addmenu(req):
    form = MenuForm()
    if req.method == 'POST':
        form = MenuForm(req.POST)
        if form.is_valid():
            form.save()
        return redirect('menu')
    return render(req, 'addmenu.html', {'form':form})



def register(req):
    if req.method == 'POST':
        firstname = req.POST.get('nname')
        email = req.POST.get('email')
        username = req.POST.get('uname')
        password = req.POST.get('passw')

        user = User.objects.filter(username=username)
        print(user)

        if user.exists():
            messages.error(req, 'username already taken!')
            return redirect('register')

        user = User.objects.create(first_name=firstname,
                    email=email,
                    username=username
                    )

        user.set_password(password)
        user.save()
        messages.success(req,'Registered Successuly!')
        return redirect('register')
        
    return render(req, 'register.html')


def loginform(req):
    if req.method=='POST':
        username = req.POST.get('uname')
        password = req.POST.get('passw')

        if not User.objects.filter(username=username).exists():
            messages.info(req, 'Invalid username!')
            return redirect('login')

        user = authenticate(req, username=username, password=password)

        if user is None:
            messages.info(req, 'invalid password')
            return redirect('login')
        
        else:
            login(req, user)
            return render(req, 'home.html')
            
        
    return render(req, 'login.html')



def logoutform(req):
    logout(req)
    return redirect('home')
