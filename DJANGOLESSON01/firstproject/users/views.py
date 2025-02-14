from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def register_view(request):
    #form = UserCreationForm()  # Ensure form is always defined

    if request.method == "POST":
        form = UserCreationForm(request.POST)  # Corrected form initialization
        if form.is_valid():
            form.save()
            return redirect("posts:list")  # Ensure 'posts:list' exists in your urls.py
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {"form": form})
