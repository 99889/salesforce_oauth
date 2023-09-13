

from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_with_salesforce, name='login_with_salesforce'),
    path('salesforce/callback/', views.salesforce_callback, name='salesforce_callback'),
]
