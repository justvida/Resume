from django.shortcuts import render

# Create your views here.
def index_view(request):
    return render(request, 'website/index.html')

def portfolio_view(request):
    return render(request, 'website/portfolio-details.html')

def service_view(request):
    return render(request, 'website/service-details.html')

def starter_view(request):
    return render(request, 'website/starter-page.html')