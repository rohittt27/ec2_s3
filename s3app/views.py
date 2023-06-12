from django.shortcuts import render, redirect
from django.views import View
from s3app.models import signup_form
from .forms import SignForm

class SignFormView(View):
    def get(self, request):
        form = SignForm()
        return render(request, 'sign_form.html', {'form': form})

    def post(self, request):
        form = SignForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'thankyou.html')
        return render(request, 'sign_form.html', {'form': form})