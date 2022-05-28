from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
User = get_user_model()
from django.contrib import messages
from django.core.mail import EmailMessage, send_mail
from django.urls import reverse, reverse_lazy
from sentoki_project import settings
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth import authenticate, login, logout
from . tokens import account_activation_token
from django.contrib.messages.views import SuccessMessageMixin
from sentoki_project import urls


# Create your views here.

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname'].lower()
        lname = request.POST['lname'].lower()
        email = request.POST['email']
        year = request.POST['year']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        b = False
        if User.objects.filter(username=username):
            messages.error(request, "Username already exists! Please try some other username.",extra_tags='username')
            b = True
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered!!",extra_tags='email')
            b = True
        
        if len(username)>20:
            messages.error(request, "Username must be under 20 charcters!!",extra_tags='username')
            b = True
        
        if pass1 != pass2:
            messages.error(request, "Passwords didn't match!!",extra_tags='pass')
            b = True
        
        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!!",extra_tags='username')
            b = True
        a = email.split('@')
        if a[1] != 'estin.dz':
            messages.error(request, "Email not valid, should be given by ESTIN",extra_tags='email')
            b = True
        else:
            if '_' not in a[0]:
                messages.error(request, "Email not valid, should be given by ESTIN",extra_tags='email')
                b = True
            else:
                z = a[0].split('_')
                if len(z[0]) != 1:
                    messages.error(request, "Email not valid, should be given by ESTIN",extra_tags='email')
                    b = True
        if b :
            return redirect('signup')
        
        myuser = User.objects.create_user(username=username, email=email)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.set_password(pass1)
        #myuser.is_active = False
        myuser.save()
        current_site = get_current_site(request)
        email_subject = "Activate your account"
        email_body = {
                    'user': myuser,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(myuser.pk)),
                    'token': account_activation_token.make_token(myuser),
        }
        link = reverse('activate', kwargs={
            'uidb64': email_body['uid'], 'token': email_body['token']})
        activate_url = 'http://'+current_site.domain+link
        email = EmailMessage(
            email_subject,
            'Hi ' + myuser.username + ', Please the link below to activate your account \n'+activate_url,
            'noreply@semycolon.com',
            [myuser.email],
        )
        email.send(fail_silently=False)
        messages.success(request, 'Account successfully created, please check your email in order to activate your account')
        
        return redirect("home")
        
        
    return render(request, "signup.html")


        


def activate(request, uidb64, token):  
    try:
        id = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=id)

        if not account_activation_token.check_token(user, token):
            return redirect('signin'+'?message='+'User already activated')
        if user.is_active:
            return redirect('signin')
        user.is_active = True
        user.save()

        messages.success(request, 'Account activated successfully')
        return redirect('signin')

    except Exception as ex:
        pass
    return redirect('signin') 


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']
        
        user = authenticate(username=username, password=pass1)
        
        if user is not None:
            login(request, user)
            return render(request, "home.html")
            # messages.success(request, "Logged In Sucessfully!!")
        else:
            messages.error(request, "Bad Credentials!!")
            return render(request, "signin.html")
    
    return render(request, "signin.html")


def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!!")
    return redirect('home')
