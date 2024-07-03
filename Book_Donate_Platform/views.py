from django.shortcuts import render
from django.views.generic import TemplateView

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


# Create your views here.


def send_contact_email(name,subject,problem,email,phone,template):
    
    message=render_to_string(template,{
        'name':name,
        'subject':subject,
        'problem':problem,
        'phone':phone,
        'email':email
    })
    
    send_email=EmailMultiAlternatives(subject,'',to=['ratin.cse@gmail.com'])
    send_email.attach_alternative(message,'text/html')
    send_email.send()


class HomeView(TemplateView):
    template_name = 'index.html'

def about_view(request):
    return render(request, 'about.html')

def contact(request):
    
    if request.method=='POST':
        
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        problem = request.POST.get('problem')
        phone = request.POST.get('phone')
        
        print(name,email,subject,phone,problem)
        
        send_contact_email(name,subject,problem,email,phone,"contact_email.html")
        
        return render(request, 'contact.html')
        
    else:
        return render(request, 'contact.html')