from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

from navbar.views import navbar

def home(request):
    # return render(request, 'navbar/nav.html')  
    return render(request, 'hotels/home.html')  
    







