from django.shortcuts import render, redirect
from django.utils.translation import gettext as _
from .models import Dictionary
from .forms import InputForm
from .forms import AddForm
from django.contrib import messages
from .utils import fill_model
from django.conf import settings
import os
from django.urls import path,reverse
import requests
from bs4 import BeautifulSoup    # importする
import pdb
import json
from .translate import get_translation
from django.http.response import JsonResponse
from django.db.models import CharField
from django.db.models import  Q

def home(request):
    # TODO: replace with second migration
    #fill_model(os.path.join(settings.BASE_DIR,"dict_page","data.json"))
    form = InputForm()
    return render(request, 'home.html')

def all_query(table,SEARCH_TERM):
    fields = [f for f in table._meta.fields if isinstance(f, CharField)]
    queries = [Q(**{f.name: SEARCH_TERM}) for f in fields]

    qs = Q()
    for query in queries:
        qs = qs | query
    return qs

def get_query(request):
    form = InputForm(request.GET)
    if form.is_valid():
        word = form.cleaned_data['word']
        qs = all_query(Dictionary,word)

        Dict = Dictionary.objects.filter(qs).first()
        if Dict is None:
            messages.error(request, _('A word was not found in the Dictionary'))
            return render(request, 'home.html', {'form' : form})
        context = {'form' : form, 'def1' : Dict.def1,'def2' : Dict.def2,
        'def3' : Dict.def3,'def4' : Dict.def4,
        'def5' : Dict.def5, 'def6' : Dict.def6,
        'def7' : Dict.def7 , 'def8' : Dict.def8 ,
        'def9' : Dict.def9 , 'def10' : Dict.def10 
        }

        return render(request, 'home.html', context)
    messages.error(request, 'Your input has error')
    return render(request, 'home.html', {'form' : form})

def about(request):
    context = {}
    return render(request, "about.html", context)

def delete(request, id):
    w = Dictionary.objects.get(id=id)
    w.delete()
    return redirect("/content") 

def content(request):
    all_words = Dictionary.objects.all
    form = AddForm(request.POST)

    if request.method == 'POST':
        if not form.is_valid():
            messages.success(request, 'You should add a word and a definition!')
            return render(request, 'content.html', {'form': form, 'all_words': all_words} )

        form.save()
        messages.success(request, 'A new word has been added to the Dictionary'  )
    
    pdb.set_trace()
    return render(request, 'content.html', {'form': form ,'all_words': all_words})

def search(request,*args,**kwargs):
    if "url" in request.GET:
        load_url = request.GET.get('url')
        html = requests.get(load_url)
        soup = BeautifulSoup(html.content, "html.parser")    # HTMLを解析する
        print(soup)

    else:
        None

    return request

def translate(request):
    data = json.loads(request.body)
    text_input = data['text']
    translation_output = data['to']
    response = get_translation(text_input, translation_output)
    return JsonResponse(response, safe=False)
