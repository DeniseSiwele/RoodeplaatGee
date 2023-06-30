# models.py
from django.db import models

class User(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    medical_aid_details = models.TextField()
    membership_type = models.CharField(max_length=20, choices=[('annual', 'Annual'), ('monthly', 'Monthly'), ('daily', 'Daily')])
    qr_code = models.CharField(max_length=100, null=True, blank=True)
    registration_date = models.DateTimeField(auto_now_add=True)

 #   def generate_qr_code(self):
        # Implement QR code generation logic here
 #       self.qr_code = generate_qr_code(self.name, self.surname)  # You would need to implement this function
 #       self.save()
