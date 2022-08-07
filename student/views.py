from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from teacher.views import add_user


# Create your views here.
def login(request):
    if 'user' in request.session:
        return redirect(dashboard)
    elif 'admin' in request.session:
        return redirect(add_user)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            
            if user.is_superuser: 
                request.session['admin'] = username
                auth.login(request, user)
                return redirect(add_user)
                # return render(request, 'admin_panel/remove_user.html')  
            else:
                request.session['user'] = username
                auth.login(request, user)
                return redirect(dashboard)
        else:
            messages.info(request,'Invalid Credintials')
            return redirect(login)
    else: 
        return render(request, 'user_login.html')
        


def user_registration(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.info(request, 'Username Taken')
            return redirect(user_registration)
        elif User.objects.filter(email=email).exists():
            messages.info(request,"Email Already taken")
            return redirect(user_registration)
        else:
            user = User.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name, email=email)
            user.save();
            return redirect(login)

    else:
        return render(request, 'user_register.html')

def logout(request):
    if 'user' in request.session:
        request.session.flush()
    elif 'admin' in request.session:
        request.session.flush()
    auth.logout(request)
    return redirect(login)

@login_required(login_url='login')
def dashboard(request):
    if 'admin' in request.session:
        return redirect("add_user")
    else:
        return render(request, "dashboard.html")
