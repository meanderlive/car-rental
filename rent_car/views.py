from django.shortcuts import render
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from .models import *
from django.db.models import Q
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import login,logout

from .forms import *
#from .forms import UserRegistrationForm,UserProfileForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .models import UserProfile
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from .models import User,  UserProfile
from django.db.models import Q
from django.urls import reverse
# Create your views here.
from django.urls import path
from django.http import HttpResponse

def simple_view(request):
    return HttpResponse('Test')

def custom_logout_view(request):
    logout(request)
    return redirect('business-register')

@login_required
def home(request):
    car_rents = CarRent.objects.all()
    return render(request,'demo-business.html', {'car_rents': car_rents})

@login_required
def about(request):
    return render(request,'demo-business-about.html')

@login_required
def clients(request):
    return render(request,'demo-business-clients.html')

@login_required
def blog(request):
    return render(request,'demo-business-blog.html')

@login_required
def contact(request):
    return render(request,'demo-business-contact.html')

@login_required
def pricing(request):
    return render(request,'demo-business-pricing.html')

@login_required
def service(request):
    return render(request,'demo-business-services.html')

@login_required
def single(request):
    return render(request,'demo-business-single-product.html')

def home_redirect(request):
    print("home_redirect called")
    if request.user.is_authenticated:
        print("User is authenticated")
        return redirect('business-home')
    else:
        print("User is not authenticated")
        return redirect('business-register')

def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('business-login')   # Redirect to the user list or any other page
            #return HttpResponse('Test')

    else:
        form = UserRegistrationForm()
    #return render(request, 'register.html', {'form': form})
    return render(request,'demo-business-register.html',{'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('profile_view')
    else:
        form = AuthenticationForm()
    return render(request, 'demo-business-login.html', {'form': form})

@login_required
def update_register(request):

    user = request.user

    if request.method == 'POST':
        form = CustomUserUpdateForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile_view')
    else:
        form = CustomUserUpdateForm(instance=user)

    return render(request, 'dev_html/demo-business-all-update.html', {'form': form,"insta": insta})


"""def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('profile_update')
    else:
        form = AuthenticationForm()
    return render(request, 'demo-business-login.html', {'form': form})
"""
@login_required
def change_password(request):

    user = request.user

    if request.method == 'POST':
        form = PasswordUpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile_view')  # Redirect to the profile page or any other page
    else:
        form = PasswordUpdateForm(instance=user)
    return render(request, 'demo-business-update.html', {'form': form})



@login_required
def update_profile(request):

    user = request.user
    try:
        user_profile = UserProfile.objects.get(user=user)
    except UserProfile.DoesNotExist:
        user_profile = UserProfile(user=user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('profile_view')  # Redirect to the profile page or any other page
    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, 'demo-business-profile.html', {'form': form})

@login_required
def get_profile(request):
    user = request.user
    try:
        user_profile = UserProfile.objects.get(user=user)
    except UserProfile.DoesNotExist:
        user_profile = None
    con={'profile': user_profile}
    return render(request, 'demo-business-get-profile.html', con)


@login_required
def delete_profile(request):

    user = request.user
    try:
        user_profile = UserProfile.objects.get(user=user)
        user_profile.delete()
        messages.success(request, 'Profile deleted successfully.')
    except UserProfile.DoesNotExist:
        messages.error(request, 'Profile does not exist.')

    return redirect('profile_view')



# List all car rentals
@login_required
def car_rent_list(request):
    car_rents = CarRent.objects.all()
    return render(request, 'demo-business-services.html', {'car_rents': car_rents})

# Create a new car rental

def car_rent_create(request):
    if request.method == 'POST':
        form = CarRentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('car_rent_list')
    else:
        form = CarRentForm()
    return render(request, 'demo-business-car_rent_form.html', {'form': form})

# Update an existing car rental
def car_rent_update(request, id):
    car_rent = get_object_or_404(CarRent, id=id)
    if request.method == 'POST':
        form = CarRentForm(request.POST, request.FILES, instance=car_rent)
        if form.is_valid():
            form.save()
            return redirect('car_rent_list')
    else:
        form = CarRentForm(instance=car_rent)
    return render(request, 'demo-business-car_rent_form.html', {'form': form})

# Delete a car rental
def car_rent_delete(request, id):
    car_rent = get_object_or_404(CarRent, id=id)
    if request.method == 'POST':
        car_rent.delete()
        return redirect('car_rent_list')
    content={'car_rent': car_rent}
    return render(request, 'car_rent_confirm_delete.html',content )

# Get car rental details by id
def car_rent_detail(request, id):
    car_rents = CarRent.objects.all()
    car_rent = get_object_or_404(CarRent, id=id)
    return render(request, 'demo-business-single-product.html', {'car_rent': car_rent,"rent":car_rents})
