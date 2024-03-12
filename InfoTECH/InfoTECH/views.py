# views.py
from django.shortcuts import render
from . import mysql_data
from .models import Subscription

def index(request):
    if request.method=='POST':
        name = request.POST.get('name', 'Default')
        email = request.POST.get('email', 'Default')
        number = request.POST.get('Phone', 'Default')
        password = request.POST.get('password', 'Default')
        course = request.POST.get('Courses', 'Default')
        language = request.POST.get('programming_language', 'Default')
        global user,data
        user = Subscription(email, password)
        data = user.send_to_index()
        if data!=False:
            return render(request,'login.html',{'login':'Already Exist'})
        else:
            mysql_data.save_data_to_mysql({
                'name': name,
                'number': number,
                'email': email,
                'password': password,
                'course': course,
                'language': language,
            })
            user = Subscription(email, password)
            data = user.send_to_index()
            return render(request, 'index.html', data)
    else:
        return render(request, 'index.html')


def login(request):
    return render(request,'login.html')

def existing_account(request):
    global user,data
    email=request.POST.get('email','Default')
    password=request.POST.get('password','Default')    
    user=Subscription(email,password)
    data=user.send_to_index()
        
    if data==False:
        return render(request, 'login.html', {'data': 'Data Not Found','refresh':'Please Refresh'})
    else:
        return render(request,'index.html',data)


def account(request):
    try:
        if data==False:
            return render(request,'login.html',{'login':'Incorrect Password or E-mail'})
        else:
            data=Subscription()
            return render(request,'account.html',data)
    except:
        return render(request,'login.html',{'login':'Please Login First'})
    
def logout(request):
    return render(request, 'index.html')