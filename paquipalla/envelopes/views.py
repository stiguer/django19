from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def mainpage(request):
    return HttpResponse('<html><body>Hello</body></html>')
