from django import forms


class StudentForm(forms.Form):
    file = forms.FileField()  # for creating file input


sid = "hello"


class Form2(forms.Form):
    firstname = forms.CharField(label="Enter first name",
                                max_length=50,
                                initial=sid)

    email = forms.EmailField(label="Enter Email")
