from django.contrib.auth import authenticate
from django.shortcuts import render
from django.views import View
from django.contrib import messages
from .models import *
from .forms import *
from django.core.mail import EmailMessage,send_mail
from medront.settings import EMAIL_HOST_USER
from django.http import HttpResponse
# Create your views here.

#class base view for the login functionality
class login(View):

    #method to handle the request type is get
    def get(self,request):
        return render(request,'login.html')
    #function to handle if the request method type is post
    def post(self,request):
        email=request.POST.get('email')
        password=request.POST.get('password')
        user=CustomUser.objects.filter(email=email,password=password)
        #print(user)

        #if user exists in the data base redirecting the user into home page of the website
        if len(user):
            phones=mobiles.objects.all()
            return render(request,'home.html',{'mobiles':phones})
        #user=CustomUser.objects.filter(email=email,password=password)

        #if user is not existed in the rendering a warining message to user and redirecting to the loginpage
        else:
            messages.warning(request,'enter details correctly')
        return render(request,'login.html')


#class based view for the functionality of the signup
class signup(View):

    #get function to handle the request method is get
    def get(self,request):
        return render(request,'register.html')

    #post method to hadle the request method is post
    def post(self,request):

        #getting the values entered by the user
        self.first_name=request.POST.get('firstname')
        print('---------------------------', self.first_name)
        self.last_name=request.POST.get('lastname')
        self.email=request.POST.get('email')
        self.password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')
        self.username=self.first_name+" "+self.last_name

        #checking if the username is already present in the database
        existed_user=CustomUser.objects.filter(username=self.username)
        print(existed_user)
        #if username is already exists showing error message to the user
        if len(existed_user):
            messages.warning(request,'username already exists!')
            return render(request, 'register.html')

        #checking if the mail is present in the database if exists showing error message to user
        if CustomUser.objects.filter(email=self.email):
            messages.warning(request,'already used this mail')
            return render(request, 'register.html')
        #checking the both passwords are matching or not
        if self.password==confirm_password:

            #sending a otp mail to the user
            subject="OTP verification code"

            import random
            randint=random.randint(100000,999999)
            print(randint)
            message="your OTP for register "+str(randint)
            o=otpForm(self.username,randint)

            o.save()

            try:
                Email=EmailMessage(subject,message,EMAIL_HOST_USER,to=[self.email])
                Email.send()

                messages.success(request,'OTP send to the {} please check in spam also'.format(self.email))
                return render(request,'otp.html')

            except Exception as e:
                messages.warning(request,"error ocuured try after some time!")

        #if passwords are not matching showing error message to user
        else:
            messages.warning(request, "passwords are not matching!")

        return render(request,'register.html')


    #save method to save the user in the database after the otp verification
    def saved(self):
        print('---------------------------',self.first_name)
        self.new_user = CustomUser.objects.create_user(first_name=self.first_name, last_name=self.last_name, username=self.username,
                                                       email=self.email, password=self.password)
        self.new_user.email = self.email
        self.new_user.password = self.password
        self.new_user.save()

#otp class inheriting the signup class to access the save method and its variables
class otp(signup):
    #function to handle the resquest method is post
    def post(self,request):
        otp=request.POST.get('otp')
        if otp=='123456':

            #calling the method of signup.save method to save the user after otp verification
            s=signup()
            s.saved()
            return render(request,'login.html',{'context':"yes"})

        return render(request,'otp.html')