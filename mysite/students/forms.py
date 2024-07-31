from django import forms
from students.models import Student
from tracks.models import Track


class StudentForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    email = forms.EmailField(label='Email', required=False)
    grade = forms.IntegerField(label='Grade', required=False)
    image = forms.ImageField(label='Image', required=False)
    # track = forms.ChoiceField(label='Track', required=False, choices={
    #     "1":'iti',  "2":"python"   })
    track = forms.ModelChoiceField(queryset=Track.objects.all(), required=False)

    # check if email exists before ??? then data not valid ??
    def clean_email(self):
        email = self.cleaned_data['email']
        # check if email not exists before in the students
        exists = Student.objects.filter(email=email).exists()
        if exists:
            raise forms.ValidationError('Email already registered before')
        else:
            return email

    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) < 3:
            raise forms.ValidationError('Name must be at least 3 characters')
        else:
            return name


    def clean_grade(self):
        grade = self.cleaned_data['grade']
        if grade:
            if grade > 100 or grade < 0:
                raise forms.ValidationError('Grade must be between 0 and 100')
            else:
                return grade


class StudentModelForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) < 3:
            raise forms.ValidationError('Name must be at least 3 characters')
        else:
            return name

    def clean_grade(self):
        grade = self.cleaned_data['grade']
        if grade:
            if grade > 100 or grade < 0:
                raise forms.ValidationError('Grade must be between 0 and 100')
            else:
                return grade