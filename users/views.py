from django.shortcuts import render,HttpResponse
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.template.context_processors import csrf 

from users.models import Users
from PicProcure.custom_azure import AzureMediaStorage
from django.contrib.auth.models import User
# Create your views here.
def register(request):
    if request.method == "POST":
        user = Users()
        user.user_name = request.POST.get('user_name','')
        user.first_name = request.POST.get('first_name','')
        user.last_name = request.POST.get('last_name','')
        user.email_id = request.POST.get('email_id','')
        user.password = request.POST.get('password','')
        repassword = request.POST.get('re-password','')
        if user.password == repassword:
            file = request.FILES.get('profile_pic')
            user.profile_pic = user.user_name
            md = AzureMediaStorage()
            #md.location= "Profile_Pics"
            md.azure_container = 'profile-pics'
            pp = md._save(user.first_name + user.last_name,file)
        user.save()
        a = User.objects.create_user(user.user_name,user.email_id,user.password)
        a.save()
        return render(request,'users/login.html')
    return render(request,'users/signup.html')

def login(request):
    c = {}
    c.update(csrf(request))
    return render(request,'users/login.html', c)

def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    try:
        user= User.objects.get(username=username)
        print(user.password)
        x = auth.authenticate(username= username,password=password)
        print(x)
        if x is not None:
            auth.login(request,x)
            print()
            request.session['user_name'] = user.username
            return render(request,'uploadFiles/base.html', {"full_name": request.session['user_name']})

        else:
            return render(request,'users/login.html', {"Invalid_msg": "Invalid Username or Password"})
    except:
        return render(request,'users/login.html', {"Invalid_msg": "Invalid Username or Password except"})

def logout(request):

    auth.logout(request)
    try:
        del request.session['user_name']
    except KeyError:
        pass
    return render(request,'users/login.html')