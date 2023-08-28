from django import forms

class CreateNewList(forms.Form):
    user_name = forms.CharField(label="Name", max_length=200)
    title = forms.CharField(max_length=200)
    completed = forms.BooleanField(required=False)

class EnterUser(forms.Form):
    name = forms.CharField(label="Name", max_length=200)