# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from forms import Search_ISBN
import json
import urllib
       
def search(request):
    if request.method =="POST":
        search_form = Search_ISBN(request.POST)
        valid_search_form = search_form.is_valid()
        if valid_search_form:
            url = "https://www.googleapis.com/books/v1/volumes?q=isbn:"+search_form.cleaned_data['isbn']
            volume = urllib.urlopen(url)
            v=volume.read()
            if(v!=""):
                j=json.loads(v)
                v_items_list = j[u'items']
                v_items = v_items_list[0]
                v_volume_info = v_items[u'volumeInfo']
                #return HttpResponse(v_volume_info[u'title'])
                return render_to_response('result.html',{'result':v_volume_info},RequestContext(request))
            #return HttpResponseRedirect("https://www.googleapis.com/books/v1/volumes?q=isbn:9780262140874")
            else:
                return HttpResponse("url returns empty string")
        else:
            return render_to_response('search.html',{'form':Search_ISBN(request.POST)},RequestContext(request))

    else:
        return render_to_response('search.html',{'form':Search_ISBN()},RequestContext(request))

