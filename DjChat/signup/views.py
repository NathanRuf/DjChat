# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def signup(request):
    if request.method == 'POST': #ensures that POST is being used
        form = UserCreationForm(request.POST)

        if form.is_valid(): #Checks if form is set
            form.save()

            #gets username and password data:
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')

            user = authenticate(username=username, password=raw_password) #creates the user
            login(request, user) #auto-logins the user

            return redirect('home')
    else: #POST is not being used
        form = UserCreationForm()

    return render( request, 'signup.html', {'form': form} )
