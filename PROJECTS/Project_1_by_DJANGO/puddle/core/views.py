from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'core/index.html')
# * It will search templates folder and then search the required address

def contact(request):
    return render(request, 'core/contact.html')