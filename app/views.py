

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

from .forms import Indexform

# def index(request):
#     if 'name' in request.GET:
#         name = request.GET['name']
#         result = 'my name is ' + name + '!!'
#     else:
#         result = 'please input query name'
#     return HttpResponse(result)

def index(request):
    #query paramater
    params = {
        'title':'Hello World',
        'msg':'ちゃんと挨拶したいので情報の登録をしてください',
        'form': Indexform(),
        'gopage':'secondindex'
    }
    if (request.method=='POST'):
        params['msg'] = 'こんにちは!'+request.POST['name']+'さん!<br>'+request.POST['area']+'にお住まいで<br>年齢は'+request.POST['age']+'歳なんですね!<br>よろしくお願いします。'
        params['form']= Indexform(request.POST)
    return render(request,'app1/index.html', params)

def second(request):
    params = {
    'title':'hello world',
    'msg':'こんにちは',
    'gopage':'index'
    }
    return render(request,'app1/index.html', params)

def form(request):
    msg = request.POST['msg']
    params = {
        'title':'Hello World',
        'msg':'hello '+msg+'!',
        'gopage':'index'
    }
    return render(request,'app1/index.html', params)

class IndexTemplateView(TemplateView):
    def __init__(self):
        self.params = {
            'title':'Hello World',
            'msg':'ちゃんと挨拶したいので情報の登録をしてください',
            'form': Indexform(),
            'gopage':'secondindex'
        }

    def get(self,request):
        return render(request,'app1/index.html',self.params)

    def post(self,request):
        msg = 'こんにちは!'+request.POST['name']+'さん!<br>'+request.POST['area']+'にお住まいで<br>年齢は'+request.POST['age']+'歳なんですね!<br>よろしくお願いします。'
        self.params["msg"] = msg
        self.params['form'] = Indexform(request.POST)
        return render(request,'app1/index.html',self.params)
