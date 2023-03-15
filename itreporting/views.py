from django.shortcuts import render
from .models import Issue

def home(request):
    #return HttpResponse('<h1> Student IT Services - Home </h1>')
    return render(request, 'itreporting/home.html', {'title': 'Home'} )
def about(request):
    return render(request, 'itreporting/about.html', {'title': 'About Us'} )
    #return HttpResponse('<h1> Student IT Services - About </h1>')
def contact(request):
   return render(request, 'itreporting/contact.html', {'title': 'contact'})
# Create your views here.

def report(request):
    daily_report= {
        'issues': Issue.objects.all()
    }

    return render(request, 'itreporting/report.html', daily_report)