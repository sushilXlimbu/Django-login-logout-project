from django.shortcuts import render,redirect
from django.http import HttpResponse    #An HTTP response is made by a server to a client.
from .models import Feature
from django.contrib.auth.models import User, auth
from django.contrib import messages


def index(request):
    feature0 = Feature()
    feature0.id = 0
    feature0.name = 'Fast track'
    feature0.details = '13Km Road Necessitatibus eius consequatur ex aliquid fuga eum quidem. Sit sint consectetur velit. Quisquam quos quisquam cupiditate. Et nemo qui impedit suscipit alias ea. Quia fugiat sit in iste officiis commodi quidem hic quas.'

    feature1 = Feature()
    feature1.id = 1
    feature1.name = 'Master trader'
    feature1.details = 'hello world my name is master trader plesase help me to be the all time greatest trader by your love and support'
    features = [feature0,feature1]
    return render(request,'index.html', {'features':features})

    #Basic way
    #name = 'Sushil'
    #return render(request,'index.html', {'Name':name})

    #Proper way
    #context = {
        #'name' : 'Sushil Master',
        #'age' : 24,
        #'phone':9810483962
    #}
    #return render(request,'index.html', context) #context is a dictionary passing to index.html

def counter(request):
    text = request.POST['text']
    amount_of_words = len(text.split())
    return render(request, 'counter.html', {'amount' : amount_of_words})  

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username') #requset.POST.get('username') this stores the value provided by the user while signin and The above handles both the POST and GET methods that may result. I hope this helped.
        email = request.POST.get('email ')
        password = request.POST.get('password')
        password2 = request.POST.get('password2') 
        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email already exists')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'Username already used')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,email= email,password= password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Password not matched')
            return redirect('register')
    else:
         return render(request,'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')

        else:
            messages.info(request, 'Username or password is not correct.')
            return redirect('login')

    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')


   

def post(request,pk):
    return render(request, 'post.html', {'pk':pk})
