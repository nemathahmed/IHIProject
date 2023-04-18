from django.forms import ModelForm
from django import forms
from .models import User, Provider, Patient
from django.db.models import CharField, Value as V
from django.db.models.functions import Concat

USER_TYPE= [
    ('PR', 'Provider'),
    ('PA', 'Patient')
    ]

class DateInput(forms.DateInput):
    input_type = 'date'

class SignUpForm(ModelForm):
    type_of_user = forms.ChoiceField(choices=USER_TYPE, widget=forms.RadioSelect())
    date_of_birth = forms.DateField(widget = DateInput, label = "Date of Birth")
    pwd = forms.CharField(widget=forms.PasswordInput(), label = "Enter Password")
    class Meta:
        model = User
        fields = ('first_name','last_name','email','pwd','repwd','type_of_user','gender','date_of_birth','phone','address',)
        labels = {'first_name':'First Name',
                    'last_name':'Last Name',
                    'email':'Email',
                    'pwd':'Enter Password',
                    'repwd':'Renter Password',
                    'type_of_user':'Type of User',
                    'gender':'Gender',
                    'date_of_birth':'Date of Birth',
                    'phone':'Phone',
                    'address':'Address',}
        exclude = ['repwd']

class LoginForm(forms.Form):
    user_name = forms.CharField(label="Username (Email Id)", max_length = 100)
    password = forms.CharField(label="Password", max_length = 15, widget=forms.PasswordInput())

class PatientDemographicsForm(forms.ModelForm):
    doctors = User.objects.filter(type_of_user = 'PR').annotate(full_name = Concat('first_name', V(' ') ,'last_name')).values_list('user_id','full_name')
    doctor_id = forms.CharField(widget = forms.Select(choices = doctors))
    patient_id = forms.CharField(widget = forms.TextInput(attrs={'readonly':'readonly'}))
    class Meta:
        model = Patient
        fields = ('patient_id','doctor_id','hospital','blood_group','height','weight','medical_allergies','medications',)
        labels = {'patient_id':"Patient ID",
                    'doctor_id':"Doctor's Name",
                    'hospital':'Hospital Name',
                    'blood_group':'Blood Group',
                    'height':'Height',
                    'weight':'Weight',
                    'medical_allergies':'Medical Allergies (if any)',
                    'medications':'Ongoing Medications (if any)',
                    }

class ProviderDemographicsForm(ModelForm):
    provider_id = forms.IntegerField(widget = forms.TextInput(attrs={'readonly':'readonly'}))
    class Meta:
        model = Provider
        fields = ('provider_id','speciality','hospital')
        labels: {
            'provider_id':'Doctor ID',
            'speciality':'Speciality',
             'hospital':'Hospital',
        }