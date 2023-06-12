from django import forms
from s3app.models import signup_form

class SignForm(forms.ModelForm):
    resume = forms.FileField()
    class Meta:
        model = signup_form
        fields = "__all__"