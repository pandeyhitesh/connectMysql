from django.db import models

from django.core.files.storage import FileSystemStorage
import datetime

from django.contrib.auth.models import User
from django_mysql.models import ListCharField
# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    category = models.CharField(max_length=200, null=False, blank=False)
    price = models.DecimalField(max_digits=4,decimal_places=2)
    description = models.TextField()
    stars = models.IntegerField()

    def __str__(self):
        return self.name

'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''



'''
    name: CsaAll
    Description: main user model
    auther: pandeyhitesh
'''
# class UserAuth(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
#     # username = models.CharField(max_length=200, unique=True)
    
#     category = models.CharField(max_length=200, null=False, blank=False)
#     price = models.DecimalField(max_digits=4,decimal_places=2)
#     description = models.TextField()
#     stars = models.IntegerField()

#     def __str__(self):
#         return self.name



'''
    name: CsaAll
    Description: main user model
    auther: pandeyhitesh
'''
class CsaAll(models.Model):

    class UserType(models.IntegerChoices):
        student = 1
        alumni = 2
        staff = 3
        Anonymous = 4

    class GenderType(models.IntegerChoices):
        female = 1
        male = 2
        other = 3
        
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=200)
    # username = models.CharField(max_length=200, unique=True)
    user_type = models.IntegerField(choices=UserType.choices)
    year_of_passing = models.IntegerField()
    hometown = models.CharField(max_length=200)
    gender = models.IntegerField(choices=GenderType.choices)
    email = models.CharField(max_length=200,unique = True)
    phone = models.CharField(max_length=20,unique = True)
    work_place = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    linkedin_id = models.CharField(max_length=200, unique = True, null = True)
    github_id = models.CharField(max_length=200, unique = True, null = True)



    class Meta:
        # Gives the proper plural name for admin
        verbose_name_plural = "CSAALL"

    def __str__(self):
        return self.name

'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''





'''
    name: Student_model
    Description: main user model
    auther: pandeyhitesh
'''
class Student_model(models.Model):
    student = models.ForeignKey(CsaAll , null=True, on_delete=models.SET_NULL)
    year_of_admission = models.DateField()
    post_nominals = ListCharField(
        base_field=models.CharField(max_length=100),
        size=6,
        max_length=(6 * 101)  # 6 * 10 character nominals, plus commas
    )


'''
    name: Student_model
    Description: main user model
    auther: pandeyhitesh
'''
class Project_model(models.Model):
    project_id = models.AutoField(primary_key=True)
    author_id = models.ManyToManyField(Student_model)
    categories = models.ManyToManyField(Project_category_model)
    project_title = models.CharField(max_length=100)
    project_subtitle = models.CharField(max_length=100)
    project_domain = models.CharField(max_length=100)
    project_logo = models.ImageField(upload_to='project_logos')
    project_description = models.CharField(max_length=300)
    project_specification = models.ManyToManyField(project_specification_model)
    

'''
    name: Project_category_model
    Description: main user model
    auther: pandeyhitesh
'''
class Project_category_model(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=50)



'''
    name: project_specification_model
    Description: main user model
    auther: pandeyhitesh
'''
class project_specification_model(models.Model):
    spec_platform = models.CharField(max_length=100)
    spec_languages = ListCharField(
        base_field=models.CharField(max_length=100),
        size=10,
        max_length=(6 * 101)  # 6 * 10 character nominals, plus commas
    )


'''
    name: NoticeModel
    Description: main user model
    auther: pandeyhitesh
'''
# fs = FileSystemStorage(location='/media/photos')
class NoticeModel(models.Model):
    header = models.CharField(max_length=200)
    published_date = models.DateTimeField(auto_now_add=True)
    notice_pdf = models.FileField(upload_to='notices',)

    class Meta:
        # Gives the proper plural name for admin
        verbose_name_plural = "Notices"

    def __str__(self):
        return self.header

'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''




'''
    name: EventModel
    Description: Model for events
    auther: pandeyhitesh
'''

class EventsModel(models.Model):
    header = models.CharField(max_length=200)
    event_date = models.DateTimeField(auto_now_add=True)
    thumbnail_image = models.ImageField(upload_to='events')
    description = models.CharField(max_length=500)

    class Meta:
        # Gives the proper plural name for admin
        verbose_name_plural = "Events"

    def __str__(self):
        return self.header
