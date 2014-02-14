from django.http import HttpResponse
from django.shortcuts import render_to_response,render
from django.views.decorators.cache import cache_page

@cache_page(60*20)
def home(request):
    return render_to_response('home.html')
