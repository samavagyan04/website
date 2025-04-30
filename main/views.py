from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from .models import *
from .forms import *
from website.settings import EMAIL_HOST_USER  # պետք է ներկրես EMAIL_HOST_USER

def HomePage(request):
    home = Home.objects.all()
    About = AboutInfo.objects.all()
    skills = SkilsInfo.objects.all()
    education = EducationInfo.objects.all()
    experiences = ExperienceInfo.objects.all()
    footer=FooterInfo.objects.all()
    form = ContactForm()
    if request.method == 'POST':
        print('-------------------------')
        form = ContactForm(request.POST)
        print(form)
        if form.is_valid():
            emaill = EmailMessage(
                subject = f'Hello {request.POST.get("name")}',
                body = 'your message has been sent successfully',
                from_email = EMAIL_HOST_USER,
                to = [request.POST.get("email")]
            )
            email_for_me = EmailMessage(
                subject=f'Նամակ {request.POST.get("name")}ից',
                body= f'''{request.POST.get("name")}, {request.POST.get("email")}, {request.POST.get("message")}''',
                from_email=EMAIL_HOST_USER,
                to = [EMAIL_HOST_USER]
            )
            email_for_me.send()
            emaill.send()
            form.save()
            return redirect('home')
        else:  
            print(form.errors)
    else:
        form = ContactForm()
    context = {
        'home': home,
        'About': About,
        'skills': skills,
        'education': education,
        'experiences': experiences,
        'footer':footer,
        'form': form,
    }

    return render(request, 'index.html', context)


def page404(request):
    return render(request,'404.html')