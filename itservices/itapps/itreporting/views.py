from django.shortcuts import render

def home(request):
    #return HttpResponse('<h1> Student IT Services - Home </h1>')
    return render(request, 'itreporting/home.html', {'title': 'Home'} )
def about(request):
    return render(request, 'itreporting/about.html', {'title': 'About Us'} )
    #return HttpResponse('<h1> Student IT Services - About </h1>')
def contact(request):
   return render(request, 'itreporting/contact.html', {'title': 'contact'})
# Create your views here.
