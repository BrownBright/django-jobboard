from django.db import models
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
class job(models.Model):
    title = models.CharField(max_length=100)
    #location
    job_type = models.CharField(max_length=15,choices=JOB_TYPE)
    description = models.TextField(max_length=1000)
    published_date = models.DateTimeField(auto_now=True)
    Vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    exper = models.IntegerField(default=0)

    def __str__(self):
        return self.title
    