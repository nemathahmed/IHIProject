from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib import messages
from .models import User
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import redirect

import joblib
import sklearn

def get_label_text(label):
    if label == 0:
        return "pre diabetes"
    elif label == 1:
        return "no diabetes"
    elif label == 2:
        return "diabetes"
    else:
        raise ValueError("Invalid prediction, try again: {}".format(label))
def convert_yes_no_to_int(answer):
    if answer == "yes":
        return 1.0
    elif answer == "no":
        return 0.0
    else:
        raise ValueError("Input must be 'yes' or 'no'")
        
def age_to_value(age_str):
    age = int(age_str)
    if age >= 18 and age <= 24:
        return 1.0
    elif age >= 25 and age <= 29:
        return 2.0
    elif age >= 30 and age <= 34:
        return 3.0
    elif age >= 35 and age <= 39:
        return 4.0
    elif age >= 40 and age <= 44:
        return 5.0
    elif age >= 45 and age <= 49:
        return 6.0
    elif age >= 50 and age <= 54:
        return 7.0
    elif age >= 55 and age <= 59:
        return 8.0
    elif age >= 60 and age <= 64:
        return 9.0
    elif age >= 65 and age <= 69:
        return 10.0
    elif age >= 70 and age <= 74:
        return 11.0
    elif age >= 75 and age <= 79:
        return 12.0
    elif age >= 80:
        return 13.0
    else:
        return None
    
def get_income_label(income):
    income = int(income)
    if income < 10000:
        return 1.0
    elif income < 15000:
        return 2.0
    elif income < 20000:
        return 3.0
    elif income < 25000:
        return 4.0
    elif income < 35000:
        return 5.0
    elif income < 50000:
        return 6.0
    elif income < 75000:
        return 7.0
    else:
        return 8.0




# Create your views here.
def index(request):
    return render(request, "diabpredict/homePage.html", {})


def signup(request):
    from .forms import SignUpForm, ProviderDemographicsForm, PatientDemographicsForm

    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = SignUpForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            user_type = form.cleaned_data["type_of_user"]
            new_form = form.save(commit=True)
            if user_type == "PA":
                form = PatientDemographicsForm(initial={"patient_id": new_form.pk})
                return render(
                    request, "diabpredict/PatientDemographics.html", {"form": form}
                )
            elif user_type == "PR":
                form = ProviderDemographicsForm(initial={"provider_id": new_form})
                return render(
                    request, "diabpredict/ProviderDemographics.html", {"form": form}
                )
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
            user = User.objects.filter(
                email=form.cleaned_data["user_name"], pwd=form.cleaned_data["password"]
            )
            if user:
                user_attr = user.values()[0]
                first_name = user_attr["first_name"]
                last_name = user_attr["last_name"]
                user_type = user_attr["type_of_user"]
                if user_type == "PA":
                    context = {"first_name": first_name, "last_name": last_name}
                    return render(request, "diabpredict/PatientDashboard.html", context)
                elif user_type == "PR":
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
            print(form)
            # redirect to a new URL:
            return HttpResponseRedirect("homePage.html")
        else:
            return render(request, "diabpredict/PatientDashboard.html", {})
    # if a GET (or any other method) we'll create a blank form
    else:
        return render(request, "diabpredict/PatientDemographics.html", {})


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
            return render(request, "diabpredict/ProviderDashboard.html", {})
    # if a GET (or any other method) we'll create a blank form
    else:
        return render(request, "diabpredict/ProviderDemographics.html", {})


def patientdashboard(request):

    if request.method == "POST":
        model = joblib.load('../adaboost_model.pkl')
        input_data = {
            "HighBP": 'yes',
            "HighChol": 'yes',
            "CholCheck": 'yes',
            "BMI": '25.0',
            "Smoker": 'yes',
            "Stroke": 'yes',
            "HeartDiseaseorAttack": 'yes',
            "PhysActivity": 'yes',
            "Fruits": 'yes',
            "Veggies":'no',
            "HvyAlcoholConsump":'yes',
            "AnyHealthcare": 'yes',
            "NoDocbcCost": 'no',
            "GenHlth": '2',
            "MentHlth": '10',
            "PhysHlth": '20',
            "DiffWalk": 'yes',
            "Sex": 'male',
            "Age": '30',
            "Education": '5',
            "Income": '20000',
        }

        preprocessed_data = {
            "HighBP": convert_yes_no_to_int(input_data["HighBP"]),
            "HighChol": convert_yes_no_to_int(input_data["HighChol"]),
            "CholCheck": convert_yes_no_to_int(input_data["CholCheck"]),
            "BMI": float(input_data["BMI"]),
            "Smoker": convert_yes_no_to_int(input_data["Smoker"]),
            "Stroke": convert_yes_no_to_int(input_data["Stroke"]),
            "HeartDiseaseorAttack": convert_yes_no_to_int(input_data["HeartDiseaseorAttack"]),
            "PhysActivity": convert_yes_no_to_int(input_data["PhysActivity"]),
            "Fruits": convert_yes_no_to_int(input_data["Fruits"]),
            "Veggies": convert_yes_no_to_int(input_data["Veggies"]),
            "HvyAlcoholConsump": convert_yes_no_to_int(input_data["HvyAlcoholConsump"]),
            "AnyHealthcare": convert_yes_no_to_int(input_data["AnyHealthcare"]),
            "NoDocbcCost": convert_yes_no_to_int(input_data["NoDocbcCost"]),
            "GenHlth": float(input_data["GenHlth"]),
            "MentHlth": float(input_data["MentHlth"]),
            "PhysHlth": float(input_data["PhysHlth"]),
            "DiffWalk": convert_yes_no_to_int(input_data["DiffWalk"]),
            "Sex": 1.0 if input_data["Sex"].lower() == "male" else 0.0,  # assuming male=1, female=0
            "Age": age_to_value(input_data["Age"]),
            "Education": float(input_data["Education"]),
            "Income": get_income_label(input_data["Income"]),
        }

        # Convert the input data to a format that the model can use for prediction
        preprocessed_data = [[preprocessed_data[key] for key in preprocessed_data]]

        # Generate the prediction using the loaded model
        prediction = model.predict(preprocessed_data)

        # Print the predicted value
        print(get_label_text(prediction))
        return render(request, "diabpredict/PatientDashboard.html", {"prediction": get_label_text(prediction)})
    else:
        return render(request, "diabpredict/PatientDashboard.html")


def providerdashboard(request):
    return render(request, "diabpredict/ProviderDashboard.html", {})

