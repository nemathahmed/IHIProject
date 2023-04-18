from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib import messages
from .models import User
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import redirect

# Create your views here.
def index(request):
    return render(request,'diabpredict/homePage.html',{})

def signup(request):
    from .forms import SignUpForm, ProviderDemographicsForm, PatientDemographicsForm
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = SignUpForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            user_type = form.cleaned_data['type_of_user']
            new_form = form.save(commit = True)
            if(user_type == 'PA'):
                form = PatientDemographicsForm(initial={'patient_id': new_form.pk })
                return render(request, "diabpredict/PatientDemographics.html", {"form": form})
            elif(user_type == 'PR'):
                form = ProviderDemographicsForm(initial={'provider_id': new_form})
                return render(request, "diabpredict/ProviderDemographics.html", {"form": form})
            # redirect to a new URL:
            else:
                return HttpResponseRedirect("homePage.html")
        else:
            form = SignUpForm()
            return render(request, "diabpredict/SignUp.html", {"form": form})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SignUpForm()
        return render(request, "diabpredict/SignUp.html", {"form": form})


def login(request):
    from .forms import LoginForm, SignUpForm
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = LoginForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            user = User.objects.filter(email = form.cleaned_data['user_name'], pwd = form.cleaned_data['password'])
            if(user):
                user_attr = user.values()[0]
                first_name = user_attr['first_name']
                last_name = user_attr['last_name']
                user_type = user_attr['type_of_user']
                if(user_type == 'PA'):
                    context = {'first_name':first_name,
                                'last_name':last_name}
                    return render(request, "diabpredict/PatientDashboard.html", context)
                elif(user_type == 'PR'):
                    return render(request, "diabpredict/ProviderDashboard.html", {})
                form = SignUpForm()
                return render(request, "diabpredict/SignUp.html", {"form": form})
            else:
                return HttpResponseRedirect("homePage.html")
        else:
            form = LoginForm()
            return render(request, "diabpredict/Login.html", {"form": form})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = LoginForm()
        return render(request, "diabpredict/Login.html", {"form": form})

def patientDemographics(request):
    from .forms import PatientDemographicsForm
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = PatientDemographicsForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            form.save()
            # redirect to a new URL:
            return HttpResponseRedirect("homePage.html")
        else:
            return render(request,'diabpredict/PatientDashboard.html',{})
    # if a GET (or any other method) we'll create a blank form
    else:
        return render(request,'diabpredict/PatientDemographics.html',{})

def providerDemographics(request):
    from .forms import ProviderDemographicsForm
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = ProviderDemographicsForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            form.save()
            # redirect to a new URL:
            return HttpResponseRedirect("homePage.html")
        else:
            return render(request,'diabpredict/ProviderDashboard.html',{})
    # if a GET (or any other method) we'll create a blank form
    else:
        return render(request,'diabpredict/ProviderDemographics.html',{})  



def patientdashboard(request):
    return render(request,'diabpredict/PatientDashboard.html',{})

def providerdashboard(request):
    return render(request,'diabpredict/ProviderDashboard.html',{})