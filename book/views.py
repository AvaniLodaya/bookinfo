# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from forms import Search_ISBN
import json
import urllib
from django.core.cache import cache
       
def search(request):
    if request.method =="POST":
        search_form = Search_ISBN(request.POST)
        valid_search_form = search_form.is_valid()
        if valid_search_form:
	    cache_key = search_form.cleaned_data['isbn']
	    cache_time = 1800
	    result = cache.get(cache_key)
	    if not result:
       		url = "https://www.googleapis.com/books/v1/volumes?q=isbn:"+search_form.cleaned_data['isbn']
	        volume = urllib.urlopen(url)
           	v=volume.read()
	        if(v!=""):
                    j=json.loads(v)
              	    v_items_list = j[u'items']
	            v_items = v_items_list[0]
                    v_volume_info = v_items[u'volumeInfo']
                    #return HttpResponse(v_volume_info[u'title'])
                    result = render_to_response('result.html',{'result':v_volume_info},RequestContext(request)) #return
            	#return HttpResponseRedirect("https://www.googleapis.com/books/v1/volumes?q=isbn:9780262140874")
            	else:
                    result = HttpResponse("url returns empty string") #returni
		cache.set(cache_key,result,cache_time)
            return result
        else:
            return render_to_response('search.html',{'form':Search_ISBN(request.POST)},RequestContext(request))

    else:
        return render_to_response('search.html',{'form':Search_ISBN()},RequestContext(request))

