from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.views.generic import TemplateView, CreateView, DetailView

from .forms import *
from .models import Profile
# Create your views here.

class UserRegistration(CreateView):
    model = User
    form_class = UserRegistrationForm

    template_name = "registration/user_form.html"

    def form_valid(self, form):
        if form.cleaned_data['password'] == form.cleaned_data['confirm_password']:
            user = form.save(commit=False)
            user.set_password(user.password)
            user.save()
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password'],
                                    )
            login(self.request, new_user)
            return redirect('/register/complete-profile')
        else:
            return super().form_valid(form)

class ProfileCompletion(CreateView):
    model = Profile
    form_class = ProfileCreationForm

    template_name = "registration/profile_form.html"

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            profile = form.save(commit=False)
            profile.user = self.request.user
            profile.save()
            return redirect('/')
        else:
            return redirect('/register/complete-profile')

class ProfileDetailView(DetailView):
    model = Profile
    template_name = "profile.htm"
class IndexView(TemplateView):
    template_name = "index.html"
