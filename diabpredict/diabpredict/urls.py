"""diabpredict URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
	path('homePage.html',views.index,name='index'),
    path('homePage.html', views.index, name="index"),
    path('SignUp.html', views.signup, name="signup"),
    path('Login.html', views.login, name="login"),
    path('PatientDemographics.html', views.patientDemographics, name="patientDemographics"),
    path('patientDemographics', views.patientDemographics, name='patientDemographics'),
    path('ProviderDemographics.html', views.patientDemographics, name="patientDemographics"),
    path('providerDemographics', views.providerDemographics, name='providerDemographics'),
    path('PatientDashboard.html', views.providerDemographics, name="providerDemographics"),
    path('ProviderDashboard.html', views.providerdashboard, name="providerdashboard"),
    path('admin/', admin.site.urls),
]
