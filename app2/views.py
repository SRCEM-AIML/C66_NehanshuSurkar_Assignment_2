from django.shortcuts import render

# Create your views here.


def services(request):
    return render(request, 'app2/services.html')

def contact(request):
    return render(request, 'app2/contact.html')
