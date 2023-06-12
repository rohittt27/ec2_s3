from django.urls import path
from .views import SignFormView

urlpatterns = [
    path('', SignFormView.as_view(), name='sign_form'),
]
