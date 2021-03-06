from django.shortcuts import render,HttpResponse,redirect
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.template.context_processors import csrf 
from users.models import Users,Events
from PicProcure.custom_azure import AzureMediaStorage
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.base_user import BaseUserManager
from django.core.mail import EmailMessage
from django.conf import settings
from uploadFiles.views import home
# Create your views here.
def register(request):
    if request.method == "POST":
        user = Users()
        user.user_name = request.POST.get('user_name','')
        try:
            z=Users.objects.get(user_name=user.user_name)
            if z is not None:
                return render(request,'users/signup.html',{"Invalid":"*Username already exisits!"})
        except:
            pass
        user.first_name = request.POST.get('first_name','')
        user.last_name = request.POST.get('last_name','')
        user.email_id = request.POST.get('email_id','')
        user.password = request.POST.get('password','')
        repassword = request.POST.get('re-password','')
        if user.password == repassword:
            file = request.FILES.get('profile_pic')
            user.profile_pic = user.user_name + '.jpg'
            md = AzureMediaStorage()
            #md.location= "Profile_Pics"
            md.azure_container = 'profile-pics'
            pp = md._save(user.user_name +'.jpg',file)
        else:
            return render(request,'users/signup.html',{"Invalid":"*password and Confirm-password dose not match"})
        user.save()
        a = User.objects.create_user(user.user_name,user.email_id,user.password)
        a.save()
        return render(request,'users/login.html')
    #u=User.objects.get()
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
            print(user)
            request.session['user_name'] = user.username
            return redirect(home)
            #return render(request,'uploadFiles/base.html')

        else:
            return render(request,'users/login.html', {"Invalid_msg": "Invalid Username or Password"})
    except:
        return render(request,'users/login.html', {"Invalid_msg": "Invalid Username or Password"})


def logout(request):

    auth.logout(request)
    try:
        del request.session['user_name']
    except KeyError:
        pass
    return redirect(home)

@login_required(login_url ='/users/login')
def change_password(request):
    if request.method == "POST":
        u = Users.objects.get(user_name = request.session['user_name'])
        old_password = request.POST.get('old-password')
        new_password = request.POST.get('new-password')
        re_enterpassword = request.POST.get('re-password')
        if old_password == u.password and new_password == re_enterpassword:
            u.password = new_password
            u.save()
            user = User.objects.get(username = u.user_name)
            user.set_password(new_password)
            user.save()
        else:
            return render(request,'users/change-password.html',{'status':'Your old password is incorrect or new password does match'})
        return render(request,'users/change-password.html',{'status':'Saved password successfully'})
    return render(request,'users/change-password.html')
    
def forgot_password(request):
    if request.method == "POST":  
        user = Users.objects.get(user_name= request.POST.get('user_name'))
        request.session['access_code'] = BaseUserManager().make_random_password(length=6)
        body = "Hello " + user.first_name + ' ' + user.last_name +',\n' + 'In response to your request for access code to change password, here is your access-code:' +  request.session['access_code']
        email = EmailMessage("About PicProcure Access Code",body,settings.EMAIL_HOST_USER, to=[user.email_id] )
        email.send()
        return render(request,'users/reset-password.html',{'mssg': "Check your mail for the access code"})
    return render(request,'users/forgot-password.html')
def reset_password(request):
    if request.method == "POST":
        access_code = request.POST.get('access_code','')
        if access_code == request.session['access_code']:
            new_password = request.POST.get('new-password','')
            re_password = request.POST.get('re-password')
            if new_password == re_password:
                user_name = request.POST.get('user_name')
                user =Users.objects.get(user_name=user_name)
                user.password = new_password
                user.save()
                u = User.objects.get(username = user_name)
                u.set_password(new_password)
                u.save()
                try:
                    del request.session["access_code"]
                except KeyError:
                    pass
                return render(request,'users/reset-password.html',{'status':"Password reset successful"})
            else:
                return render(request,'users/reset-password.html',{'status':"Password not matching or incorrect format"})
        else:
            return render(request,'users/reset-password.html',{'status':"Access Code Incorrect or expired"})


@login_required(login_url ='/users/login')
def view_profile(request):
    user=Users.objects.get(user_name=request.session['user_name'])
    print(user.profile_pic)
    #count=Events.objects.get(event_owner=user.user_id).count()
    return render(request,'users/profile.html',{'user':user})

@login_required(login_url ='/users/login')
def view_update_user(request):
    user = Users.objects.get(user_name=request.session['user_name'])
    if request.method == "POST":
        user.first_name = request.POST.get('first_name','')
        user.last_name = request.POST.get('last_name','')
        email_id = request.POST.get('email_id','')
        if user.email_id != email_id:
            email = EmailMessage("About Your Email Change","This is to verify your mail",settings.EMAIL_HOST_USER,to=[email_id])
            temp = email.send() 
            if temp is None:
                return HttpResponse("Error")
            user.email_id = email_id
            u = User.objects.get(username=user.user_name)
            u.email = email_id
            u.save()
        user.save()
        return render(request,'users/profile.html',{'user':user})
    return render(request,'users/edit-profile.html',{'user':user})

def feedback(request):
    if request.method == "POST":
        user=Users.objects.get(user_name=request.session['user_name'])
        body= user.user_name + request.POST.get('description','')
        email = EmailMessage("Here is my Feedback:  " ,body,settings.EMAIL_HOST_USER, to=[settings.EMAIL_HOST_USER] )
        email.send()
    return render(request,'uploadFiles/base.html',{"send":"send"})

def delete_user(request):
    users = Users.objects.get(user_name= request.session['user_name'])
    user = User.objects.get(username= request.session['user_name'])
    md= AzureMediaStorage()
    md.azure_container = 'profile-pics'
    md.delete(str(users.profile_pic))
    users.delete()
    user.delete()
    try:
        del request.session['user_name']
    except KeyError:
        pass
    return redirect(home)
