from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.models import User
from student import views


# Create your views here.


# @login_required(login_url='login')
# def add_user(request):
#     return render(request, "admin_panel/add_user.html")

# Updating Userdata with two html pages


@login_required(login_url='login')
def edit_user(request, id):
    if 'user' in request.session:
        return redirect("dashboard")
    else:
        students = User.objects.get(id=id)
        return render(request, "admin_panel/edit_user.html", {'students': students})


@login_required(login_url='login')
def view_user(request):
    if 'user' in request.session:
        return redirect("dashboard")
    else:
        students = User.objects.all().order_by('id')
        return render(request, "admin_panel/view_user.html", {'students': students})

# user deletion


@login_required(login_url='login')
def remove_user(request, id):
    students = User.objects.get(id=id)
    students.delete()
    return redirect('view_user')


@login_required(login_url='login')
def add_user(request):
    if 'user' in request.session:
        return redirect("dashboard")
    else:
        if request.method == 'POST':
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']

            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect(add_user)
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email Already taken")
                return redirect(add_user)
            else:
                user = User.objects.create_user( 
                    username=username, password=password, first_name=first_name, last_name=last_name, email=email)
                user.save()
                messages.info(request, 'User Added Successfully')
                return render(request, 'admin_panel/add_user.html')

        else:
            return render(request, 'admin_panel/add_user.html')


@login_required(login_url='login')
def update_user(request, id):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']

        students = User.objects.get(id=id)

        if students.username != username and User.objects.filter(username=username).exists():
            messages.info(request, 'Username Taken')
            return redirect('edit_user', id=id)
        elif students.email != email and User.objects.filter(email=email).exists():
            messages.info(request, "Email Already taken")
            return redirect('edit_user', id=id)

        else:
            students = User.objects.get(id=id)

            students.first_name = first_name
            students.last_name = last_name
            students.email = email
            students.username = username

            students.save()
            messages.info(request, 'User Added Successfully')
            return redirect(view_user)

    else:
        return redirect(view_user)
