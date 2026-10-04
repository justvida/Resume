
from django.urls import path
from firstsite.views import index_view, starter_view, service_view, portfolio_view

app_name = 'website'

urlpatterns = [
    path('', index_view, name= 'index'),
    path('starter', starter_view, name= 'starter'),
    path('service', service_view, name= 'service'),
    path('portfolio', portfolio_view, name= 'portfolio'),
]