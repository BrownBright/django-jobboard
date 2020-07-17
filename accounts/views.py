from django.shortcuts import render , redirect , reverse
from .forms import signuo_FORM , UserForm , ProfileForm
from django.contrib.auth import authenticate , login
from .models import profile 

# Create your views here.



def signup(request):
    if request.method == "POST":
        form = signuo_FORM(request.POST)
        if form.is_valid:
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request,user)
            return redirect('/accounts/profile')
    else:
        form = signuo_FORM()

    return render(request,'registration/signup.html',{'form' : form})


def Profile(request):
    profilo = profile.objects.get(user=request.user)

    return render(request,'accounts/profile.html',{'profile' : profilo})

def profileedit(request):
    profilo = profile.objects.get(user=request.user)
    if request.method == "POST":
            userform = UserForm(request.POST,instance=request.user)
            ProfileForm2 = ProfileForm(request.POST,request.FILES,instance=profilo)
            if userform.is_valid and ProfileForm2.is_valid():
                userform.save()
                my_pro = ProfileForm2.save(commit=False)
                my_pro.user = request.user
                my_pro.save()
                return redirect(reverse('accounts:profile'))
    else :
            userform = UserForm(instance=request.user)
            ProfileForm2 = ProfileForm(instance=profilo)
    return render(request,'accounts/profile_edit.html',{'userform' : userform , 'ProfileForm2' : ProfileForm2})