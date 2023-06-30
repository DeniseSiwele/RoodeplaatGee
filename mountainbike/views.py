from django.shortcuts import render, redirect
from .models import User

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def gallery(request):
    return render(request, 'gallery.html')

def restaurant(request):
    return render(request, 'restaurant.html')

def signup(request):
    return render(request, 'signup.html')

def membership(request):
    return render(request, 'membership.html')

def contact(request):
    return render(request, 'contact.html')

def register(request):
    if request.method == 'POST':
        # Retrieve user details from the form
        name = request.POST['name']
        surname = request.POST['surname']
        age = request.POST['age']
        gender = request.POST['gender']
        date_of_birth = request.POST['date_of_birth']
        medical_aid_details = request.POST['medical_aid_details']
        membership_type = request.POST['membership_type']

        # Save the user details to the database
        user = User.objects.create(
            name=name,
            surname=surname,
            age=age,
            gender=gender,
            date_of_birth=date_of_birth,
            medical_aid_details=medical_aid_details,
            membership_type=membership_type
        )

        # Generate QR code
        user.generate_qr_code()
        
        # Redirect to the QR code page
        return redirect('qr_code')

    return render(request, 'register.html')