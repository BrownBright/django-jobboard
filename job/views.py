from django.shortcuts import render
from .models import job

# Create your views here.

def job_list(request):
    job_list = job.objects.all()
    max = job.objects.all().order_by("-id")[0]
    context = {'jobs' : job_list ,
                'max' : max}
    return render(request,'job/job_list.html',context)

def job_details(request , id):
    job_detail = job.objects.get(id=id)
    context = {'job' : job_detail}
    return render(request,'job/job_details.html',context)
