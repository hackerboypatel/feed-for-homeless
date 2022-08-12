from distutils.command.upload import upload
from email.policy import default
from pickle import TRUE
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image
from datetime import date
from django import forms
from django.core.exceptions import ValidationError

from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField
from django.core.validators import MinValueValidator, MaxValueValidator


#create your models here.

def validate_digit_length(phone):
    if not (phone.isdigit() and len(phone) == 10):    
        raise ValidationError('Enter a valid 10 digit  phone number ', params={'phone': phone},)



def validate_name(value):
    #string = "jistendarpatidar1"
    s1 = 0

    if all(x.isalpha() or x.isspace() for x in value):
        s1 = "yes"
    else:
        s1 = "no"

    if s1 == "yes":
        return value
    else:
        raise ValidationError("Enter a valid name")
 



class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    contact_name = models.CharField(
                         max_length = 200,
                         validators =[validate_name]
                         )
   
   # contact_number = models.PositiveIntegerField(validators=[validate_phone_number])
    contact_number = models.CharField(verbose_name="Phone number", max_length=10,  
    validators=[validate_digit_length])
  
    date = models.DateField(null=True, default = timezone.now ) 
    date_posted = models.DateTimeField(default = timezone.now)
    #status = models.CharField(max_length=100)
    image = models.ImageField(upload_to='food_pics', blank=False)
    #state = models.CharField(max_length=100,null=TRUE)
    state_choices = (("Andhra Pradesh","Andhra Pradesh"),("Arunachal Pradesh ","Arunachal Pradesh "),("Assam","Assam"),("Bihar","Bihar"),("Chhattisgarh","Chhattisgarh"),("Goa","Goa"),("Gujarat","Gujarat"),("Haryana","Haryana"),("Himachal Pradesh","Himachal Pradesh"),("Jammu and Kashmir ","Jammu and Kashmir "),("Jharkhand","Jharkhand"),("Karnataka","Karnataka"),("Kerala","Kerala"),("Madhya Pradesh","Madhya Pradesh"),("Maharashtra","Maharashtra"),("Manipur","Manipur"),("Meghalaya","Meghalaya"),("Mizoram","Mizoram"),("Nagaland","Nagaland"),("Odisha","Odisha"),("Punjab","Punjab"),("Rajasthan","Rajasthan"),("Sikkim","Sikkim"),("Tamil Nadu","Tamil Nadu"),("Telangana","Telangana"),("Tripura","Tripura"),("Uttar Pradesh","Uttar Pradesh"),("Uttarakhand","Uttarakhand"),("West Bengal","West Bengal"),("Andaman and Nicobar Islands","Andaman and Nicobar Islands"),("Chandigarh","Chandigarh"),("Dadra and Nagar Haveli","Dadra and Nagar Haveli"),("Daman and Diu","Daman and Diu"),("Lakshadweep","Lakshadweep"),("National Capital Territory of Delhi","National Capital Territory of Delhi"),("Puducherry","Puducherry") )

    state = models.CharField(choices=state_choices,max_length=255, null=True, blank=False)
    city  = models.CharField(max_length=100,null=TRUE)
    status = models.CharField(max_length=100,default='Available')
    booked = models.CharField(max_length=200,null=TRUE)
    file = models.FileField(null=True, blank=True ,upload_to='Files', )

    def __str__(self):
        return self.title  

    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'pk' : self.pk})
    if image == True :
        def save(self):
                super().save()
                img = Image.open(self.image.path)
                if img.height > 400 or img.width > 300:
                    output_size = (400,300)
                    img.thumbnail(output_size)
                    img.save(self.image.path)
