from django.shortcuts import render
from django.conf import settings
from django.contrib.auth.decorators import login_required
# Create your views here.
 

@login_required

def login_with_salesforce(request):
    oauth_url = f'https://login.salesforce.com/services/oauth2/authorize?client_id={settings.SALESFORCE_CLIENT_ID}&redirect_uri={settings.SALESFORCE_REDIRECT_URI}&response_type=code'
    return render(request, 'login_with_salesforce.html', {'oauth_url': oauth_url})


def salesforce_callback(request):
    code = request.GET.get('code')
    
    # Exchange the code for an access token and other information
    import requests
    data = {
        'grant_type': 'authorization_code',
        'client_id': settings.SALESFORCE_CLIENT_ID,
        'client_secret': settings.SALESFORCE_CLIENT_SECRET,
        'redirect_uri': settings.SALESFORCE_REDIRECT_URI,
        'code': code,
    }
    
    response = requests.post('https://login.salesforce.com/services/oauth2/token', data=data)
    
    if response.status_code == 200:
        # Successfully received OAuth tokens
        oauth_data = response.json()
        access_token = oauth_data['access_token']
        refresh_token = oauth_data['refresh_token']
        instance_url = oauth_data['instance_url']
        
        
        return render(request, 'welcome.html')
    else:
        
        return render(request, 'oauth_error.html')
