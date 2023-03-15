from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from myapp.models import App, User


def login_view(request):
    if request.method == 'POST':      
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')  
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    else:
        return render(request, 'login.html')


def signup_view(request):
    if request.method == 'POST':  
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')  
        else:
            return render(request, 'signup.html', {'error': 'Invalid username or password','form':form})
    
    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})


def admin(request):
    dicts={}
    apps = App.objects.all()
    if apps:
        dicts={'apps':apps}
    return render(request, 'admin.html', dicts)

def addapps(request):
    if request.method == 'POST':
        app_name = request.POST.get('appname')
        points = request.POST.get('points')


        ans=App.objects.filter(name=app_name)
        if ans:
            ans.update(points=points)
        else:
            new_app = App()
            new_app.name = app_name
            new_app.points = points

            new_app.save()
        return redirect('admin')
    return render(request, 'admin.html', {'addapps':1})


def user(request):
    apps = App.objects.all()
    return render(request, 'user.html', {'apps': apps})

def home(request):
    apps = App.objects.all()
    return render(request, 'user.html', {'apps': apps})

def openapp(request,href_value):

    my_object = App.objects.filter(name=href_value).first()
    username = request.user.username
    if request.method == 'POST':     
        new_object = User.objects.create(name=username, app=href_value, points=my_object.points)
        new_object.save()
    ans  = User.objects.filter(name=username, app=href_value).first()
    
    if ans:
        return render(request, 'openapp.html', {'name':href_value,'points':my_object.points, 'paid':1})
    
    return render(request, 'openapp.html',{'name':href_value,'points':my_object.points}) 


def task(request):
    username = request.user.username
    ans  = User.objects.filter(name=username).all()
    dict={}
    
    if ans:
        dict={'task':ans}
    return render(request, 'task.html',dict) 

def points(request):
    username = request.user.username
    ans  = User.objects.filter(name=username).all()
    point = 0
    if ans:
        for i in ans:
            point+=i.points
    return render(request, 'points.html',{'points':point}) 
    

def logout_view(request):
    logout(request)
    return redirect('/')

