from django.shortcuts import render
from words.models import Word
from words.forms import WordForm

def index(request):
    context={}
    form =WordForm()
    words=Word.objects.all()
    context['words']=sorted(words,key=lambda x: x.word)
    context['form']= form
    return render(request,'index.html',context)

def about(request):
    return render(request,'about.html')
