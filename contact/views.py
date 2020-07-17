from django.shortcuts import render

# Create your views here.


def send_me_mail(request):
    print('Happy')
    return render(request,'accounts/contact-us.html',{})