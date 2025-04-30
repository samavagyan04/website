from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Home(models.Model):
    name=models.CharField('name',max_length=255)
    profession=models.TextField('text')

class AboutInfo(models.Model):
    img=models.ImageField('img',upload_to='img',null=True)
    about = models.TextField('About',null=True)
    name=models.CharField('name',max_length=255,null=True)
    birthday = models.DateField('Birthday',null=True)
    address = models.CharField('Address',max_length=255,null=True)
    email = models.EmailField('Email',null=True)
    phone = PhoneNumberField('Phone',null=True)

    def __str__(self) -> str:
        return self.name

class SkilsInfo(models.Model):
    names=models.CharField('names',max_length=255,null=True)
    percent=models.IntegerField('percent',null=True)


class EducationInfo(models.Model):
    start_year=models.IntegerField('start_year')
    end_year=models.IntegerField('end_year')
    degree_univer=models.TextField('univer')
    faculty=models.TextField('faculty')
    description=models.TextField('description')


class ExperienceInfo(models.Model):
    start_year=models.IntegerField('start_year')
    end_year=models.IntegerField('end_year')
    experience=models.TextField('experience ')
    univer=models.TextField('univer')
    description=models.TextField('description')


class ContactModel(models.Model):
    name = models.CharField('Your name',max_length=255)
    email = models.EmailField('Your Email')
    message = models.TextField('Message')

    def __str__(self):
        return self.name
    
class FooterInfo(models.Model):
    facebook = models.URLField('facebook')
    github=models.URLField('GitHub')
    instagram=models.URLField('instagram')
    linkedin = models.URLField('linkedin')






