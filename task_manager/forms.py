
from django import forms
from django.core.exceptions import ValidationError
from task_manager.models import Login, SignUp, Task


class LoginForm(forms.ModelForm):

    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Employee', 'Employee'),
    ]
    role = forms.ChoiceField(choices=ROLE_CHOICES)
    class Meta:
        model = Login
        fields = ['username','password']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter Your name : '}),
            'password': forms.PasswordInput(attrs={'class':'form-control', 'placeholder': 'Enter your Password : '}),
        }

class SignUpForm(forms.ModelForm):
    next_password = forms.CharField(
        max_length=15,
        widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Re-enter Your Password : '})
    )
    class Meta:
        model = SignUp
        fields = '__all__'
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Username : ' }),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter Password : '}) ,
            'birthdate': forms.DateInput(attrs={'type':'date' , 'class':'form-control'}),
            'gender': forms.Select(choices=[('Male','Male'), ('Female', 'Female')], attrs={'class': 'form-control'}),
            'mail': forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter mail : '}) ,
            'contact': forms.NumberInput(attrs={'class': 'form-control','placeholder':'Enter Your Phone.No : '}),
            'address': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your address : '})
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        next_password = cleaned_data.get('next_password')

        if password and next_password and password != next_password:
            raise ValidationError('Password do not match....')
        return cleaned_data

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields['project_manager'] = forms.ModelChoiceField(
            queryset=Login.objects.filter(role='Employee'),
            empty_label='Select Project Manager'
        )
