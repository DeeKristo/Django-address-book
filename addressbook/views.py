from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import MyaddressForm
from .models import Myaddress
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.conf import settings


# Create your views here.
def home(request):
    contacts = list(Myaddress.objects.values())
    return render(request, "addressbook/index.html", {'contacts': contacts})

@login_required(login_url=settings.LOGIN_REDIRECT_URL)
def searchAddress(request):
    print('request', request.method)
    search_cond = request.GET.get('addresssearch', None)
    if search_cond:
        contacts = list(Myaddress.objects.filter((Q(fname__icontains=search_cond)|
                                            Q(lname__icontains=search_cond)|
                                            Q(phone__icontains=search_cond)|
                                            Q(address__icontains=search_cond)|
                                            Q(relationship__icontains=search_cond))&
                                            Q(parent_id=request.user.id)))
    return render(request, "addressbook/index.html", {'contacts': contacts})


def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if User.objects.filter(username=username):
            messages.error(request, "Username already exist! Please try some other username.")
            return redirect('home')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered!!")
            return redirect('home')

        if len(username) > 20:
            messages.error(request, "Username must be under 20 charcters!!")
            return redirect('home')

        if pass1 != pass2:
            messages.error(request, "Passwords didn't matched!!")
            return redirect('home')


        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request,"Your Account has been created succesfully!!!")
        return redirect('signin')

    return render(request, "addressbook/signup.html")

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            fname = user.first_name
            messages.success(request, "Logged In Sucessfully!!")
            return redirect('home')
        else:
            messages.error(request, "Bad Credentials!!")
            return redirect('home')

    return render(request, "addressbook/signin.html")

@login_required(login_url=settings.LOGIN_REDIRECT_URL)
def signout(request):
    logout(request)
    #messages.success(request, "Logged Out Successfully!!")
    return redirect('home')

@login_required(login_url=settings.LOGIN_REDIRECT_URL)
def createAddress(request):

    user=request.user
    # user_main = get_object_or_404(User,pk=user.id)
    user_record=get_object_or_404(User,pk=user.id)
    form = MyaddressForm(request.POST)
    if form.is_valid():
        form_instance=form.save(commit=False)
        form_instance.parent = user_record
        form.save()
        # myuser = User.objects.create_user(form_instance.fname,None, None)
        # myuser.first_name = form_instance.fname
        # myuser.last_name = form_instance.lname
        # myuser.save()
        return redirect('home')

    return render(request, "addressbook/create_contact.html", {'form':form})

@login_required(login_url=settings.LOGIN_REDIRECT_URL)
def deleteAddress(request, id):

    if request.method == "POST":
        address = Myaddress.objects.get(pk=id)
        address.delete()
    return redirect('home')

@login_required(login_url=settings.LOGIN_REDIRECT_URL)
def updateAddress(request, id):
    user = request.user
    user_record = get_object_or_404(Myaddress, pk=id)
    form = MyaddressForm(request.POST)
    new_data = {}
    new_data['fname']=request.POST.get('fname', None)
    new_data['lname'] = request.POST.get('lname', None)
    new_data['phone'] = request.POST.get('phone', None)
    new_data['address'] = request.POST.get('address', None)
    new_data['relationship'] = request.POST.get('relationship', None)

    if form.is_valid():
        Myaddress.objects.filter(Q(parent_id=request.user.id) & Q(id=user_record.id)).update(**new_data)
        return redirect('home')
    return render(request, "addressbook/update_contact.html", {'form': form})



