from django.db import models
from django.utils.text import slugify
import datetime
from django.contrib.auth.models import User


'''
# Create your models here.
# django model fields
#  -html widght
#  -validation
#  -db size
'''


JOB_TYPE = (
    ('Full time' , 'Full time'),
    ('Part time' , 'Part time')
)

def image_upload(instance, filename):
    Imagename , extention = filename.split('.')
    return "jobs/%s/%s.%s"%(instance.id,instance.id,extention)


class job(models.Model):
    owner = models.ForeignKey(User,related_name='job_owner',on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    #location
    job_type = models.CharField(max_length=15,choices=JOB_TYPE)
    description = models.TextField(max_length=1000)
    published_date = models.DateTimeField(auto_now=True)
    Vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    exper = models.IntegerField(default=0)
    category = models.ForeignKey('Category',on_delete=models.SET_DEFAULT,default=1)
    image = models.ImageField(upload_to=image_upload)
    slug = models.SlugField(blank=True , null=True)

    def __str__(self):
        return self.title
    
    def save(self,*args, **kwargs):
        ##logic
        self.slug = slugify(str(self.title) + ' ' + str(self.published_date.strftime("%b %d %H %M %S")))
        super(job, self).save(*args, **kwargs) # Call the real save() method



class Category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Apply(models.Model):
    job             =   models.ForeignKey(job,related_name='apply_job',on_delete=models.CASCADE)
    name            =   models.CharField(max_length=50)
    email           =   models.EmailField(max_length=120)
    link            =   models.URLField()
    cv              =   models.FileField(upload_to='apply/')
    cover_letter    =   models.TextField(max_length=500)
    created_at      =   models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name
    
