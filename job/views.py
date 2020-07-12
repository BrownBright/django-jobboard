from django.shortcuts import render ,redirect 
from django.urls import reverse
from .models import job
from django.core.paginator import Paginator
from .forms import ApplyForm , post_job
import datetime

# Create your views here.

def job_list(request):
    job_list = job.objects.get_queryset().order_by('id')
    max = job.objects.all().order_by("-id")[0]
    paginator = Paginator(job_list, 4) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'jobs' : page_obj ,
                'max' : max}
    return render(request,'job/job_list.html',context)



def job_details(request , slug):
    job_detail = job.objects.get(slug=slug)

    if request.method =='POST':
        form = ApplyForm(request.POST , request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.job = job_detail
            myform.save()
    else:
        form = ApplyForm()

    context = {'job' : job_detail , 'form' : form}
    return render(request,'job/job_details.html',context)



def add_job(request):
    if request.method =='POST':
        formpost = post_job(request.POST , request.FILES)
        if formpost.is_valid():
            myform2 = formpost.save(commit=False)
            myform2.owner = request.user
            myform2.published_date = datetime.datetime.now()
            myform2.save()
            return redirect(reverse('jobs:job_list'))
    else:
        formpost = post_job()
    return render(request,'job/add_job.html',{'formpost' : formpost})