from django.shortcuts import render

# Create your views here.
def drivers_page(request):
    return render(request, 'drivers.html')