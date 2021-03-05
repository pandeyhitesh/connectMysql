from django.db import models

from django.core.files.storage import FileSystemStorage
import datetime
# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    category = models.CharField(max_length=200, null=False, blank=False)
    price = models.DecimalField(max_digits=4,decimal_places=2)
    description = models.TextField()
    stars = models.IntegerField()

    def __str__(self):
        return self.name


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
        

    name = models.CharField(max_length=200)
    username = models.CharField(max_length=200, unique=True)
    user_type = models.IntegerField(choices=UserType.choices)
    date_of_passing = models.IntegerField(max_length=4)
    hometown = models.CharField(max_length=200)
    gender = models.IntegerField(choices=GenderType.choices)
    email = models.CharField(max_length=200,unique = True)
    phone = models.CharField(max_length=200,unique = True)
    work_place = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    linkedin_id = models.CharField(max_length=200, unique = True)
    linkedin_id = models.CharField(max_length=200, unique = True, null = True)



    class Meta:
        # Gives the proper plural name for admin
        verbose_name_plural = "CSAALL"

    def __str__(self):
        return self.name



'''
    name: NoticeModel
    Description: main user model
    auther: pandeyhitesh
'''
# fs = FileSystemStorage(location='/media/photos')
class NoticeModel(models.Model):
    header = models.CharField(max_length=200)
    published_date = models.DateTimeField(auto_now=True,default=datetime.now)
    notice_pdf = models.FileField(upload_to='notices',)

    class Meta:
        # Gives the proper plural name for admin
        verbose_name_plural = "Notices"

    def __str__(self):
        return self.header



'''
    name: NoticeModel
    Description: main user model
    auther: pandeyhitesh
'''

class EventsModel(models.Model):
    header = models.CharField(max_length=200)
    event_date = models.DateTimeField(auto_now=True,default=datetime.now)
    thumbnail_image = models.ImageField(upload_to='notices')
    description = models.CharField(max_length=500)

    class Meta:
        # Gives the proper plural name for admin
        verbose_name_plural = "Events"

    def __str__(self):
        return self.header
