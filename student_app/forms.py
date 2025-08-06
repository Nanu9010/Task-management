
from django import forms
from student_app.models import Student, SignUp ,Login


class AddStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name','std','science','maths','english']
        widgets = {
            'name': forms.TextInput(attrs={'title': 'Name' ,'placeholder': 'Enter your name : '}),
            'std': forms.Select(attrs={'title':'standard'}),
            'science':forms.NumberInput(attrs={'title':'science','placeholder':'Enter science marks : '}),
            'maths': forms.NumberInput(attrs={'title':'maths','placeholder':'Enter maths marks : '}),
            'english': forms.NumberInput(attrs={'title':'english','placeholder':'Enter english marks : '}),

        }





class LoginForm(forms.ModelForm):
    class Meta:
        model = Login
        fields = ['user_id','password']
        widgets = {
            'user_id': forms.TextInput(attrs={'title': 'username','placeholder':'Enter user_id : '}),
            'password': forms.PasswordInput(attrs={'title':'password','placeholder':'Enter Password : '}),

        }
        def __str__(self):
            return self.cleaned_data.get('user_id','password')


class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = '__all__'
        widgets = {
            'user_id': forms.TextInput(attrs={'title':'username','placeholder':'Enter user_id : '}),
            'password': forms.PasswordInput(attrs={'title':'password','placeholder':'Enter Password : '}),
            'gender': forms.Select(choices=[('Male','Male'),('Female','Female')]),
            'contact': forms.NumberInput(attrs={'title':'contact','placeholder':'Enter Phone.No : '}),
            'teacher': forms.CheckboxInput(attrs={'title':'teacher'}),
            'principle': forms.CheckboxInput(attrs={'title':'principle'}),
        }
        def __str__(self):
            return self.cleaned_data.get('user_id','password')





# class ViewStudents(forms.ModelForm):
#     class Meta:
#         model = View
#         fields = '__all__'
#         widgets = {
#             'name': forms.TextInput(attrs={'title': 'Name', 'placeholder': 'Enter your name : '}),
#             'std': forms.Select(
#                 attrs={'title':'standard'}
#             ),
#             'science': forms.NumberInput(attrs={'title': 'science', 'placeholder': 'Enter science marks : '}),
#             'maths': forms.NumberInput(attrs={'title': 'maths', 'placeholder': 'Enter maths marks : '}),
#             'english': forms.NumberInput(attrs={'title': 'english', 'placeholder': 'Enter english marks : '}),
#             'percentage': forms.NumberInput(attrs={'title': 'percentage'})
#         }

# [('I','I'),('II', 'II'),('III','III'),('IV','IV'),('V','V'),('VI','VI'),('VII','VII'),('VII','VII'),('XI','XI'),('X','X')],default= 'I'