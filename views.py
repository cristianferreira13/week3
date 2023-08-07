from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def home_view(request):
    return render(request, 'home.html')

def login_view(request):
    if request.method == 'POST':
        
        username = request.POST.get('username')
        password = request.POST.get('password')

       
        user = authenticate(request, username=username, password=password)

        
        if user is not None:
            # Log the user in
            login(request, user)

            # Redirect to the home page (change 'home' to the name of your home URL pattern)
            return redirect('home')
        else:
            # If authentication fails, show an error message
            error_message = 'Invalid username or password. Please try again.'
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')
    

