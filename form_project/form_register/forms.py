from django import forms
from .models import Principal, Teacher, Student

class PrincipalForm(forms.ModelForm):
    class Meta:
        model = Principal
        fields = ('fullname', 'message', 'code', 'position')
        labels = {
            'fullname': 'Full Name',
            'code': 'School Code',
            'position': 'Location'
        }
    
    def __init__(self, *args, **kwargs):
        super(PrincipalForm,self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = "Select Location"
        
        self.fields['fullname'].required = True
        self.fields['message'].required = True
        self.fields['position'].required = True
        self.fields['code'].required = True

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ('fullname', 'message', 'code', 'position')
        labels = {
            'fullname': 'Full Name',
            'code': 'School Number',
            'position': 'Location'
        }
    
    def __init__(self, *args, **kwargs):
        super(TeacherForm,self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = "Select Location"
        
        self.fields['fullname'].required = True
        self.fields['message'].required = True
        self.fields['position'].required = True
        self.fields['code'].required = True

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('fullname', 'message', 'code', 'position')
        labels = {
            'fullname': 'Full Name',
            'code': 'School Number',
            'position': 'Location'
        }
    
    def __init__(self, *args, **kwargs):
        super(StudentForm,self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = "Select Location"
        
        self.fields['fullname'].required = True
        self.fields['message'].required = True
        self.fields['position'].required = True
        self.fields['code'].required = True