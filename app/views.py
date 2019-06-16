

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.db.models import Q

from .forms import Indexform
from .forms import IdKensaku
from .forms import KenkoRecord
from .forms import Kensaku
from .models import Task
from .models import Touroku

def index(request):

    tasks = Task.objects.all()
    params = {
           'title':'生活データ',
           'msg':'all records',
           'form':IdKensaku(),
           'data':[],
       }

    if (request.method =='POST'):
        nametxt = request.POST['name']
        item = Touroku.objects.get(name = nametxt)
        params['data'] = [item]
        params['form'] = IdKensaku(request.POST)
    else:
        # params['data'] = Task.objects.all()
        params['data'] = Touroku.objects.all()
    return render(request,'app1/index.html', params)

def create(request):

    params = {
        'title':'生活データ',
        'msg':'入力してください',
        'form':KenkoRecord(),
        }

    if (request.method =='POST'):
        obj = Touroku()
        record = KenkoRecord(request.POST, instance = obj)
        record.save()
        return redirect(to='/app')
    return render(request, 'app1/create.html',params)

def edit(request,number):
    obj = Touroku.objects.get(id = number)
    if (request.method =='POST'):
        record = KenkoRecord(request.POST, instance = obj)
        record.save()
        return redirect(to='/app')
    params = {
        'title':'生活データ',
        'id':number,
        'form':KenkoRecord(),
    }
    return render(request, 'app1/edit.html',params)

def delete(request,number):

    record = Touroku.objects.get(id = number)
    if (request.method =='POST'):
        record.delete()
        return redirect(to='/app')
    params = {
        'title':'生活データ',
        'msg':"こちらのデータを削除しますか？",
        'id':number,
        'obj':record,
    }
    return render(request, 'app1/delete.html',params)

def find(request):
    if (request.method =='POST'):
        msg = '検索結果：'
        form = Kensaku(request.POST)
        str1 = request.POST['findname']
        str2 = request.POST['findstatus']
        data = Touroku.objects.filter(Q(name__icontains=str1) |Q(kenkobody__icontains=str2))
    else:
        msg = ''
        form = Kensaku()
        data = Touroku.objects.all()

    params = {
        'title':"生活データ",
        'msg':msg,
        'form':form,
        'data':data,
    }

    return render(request, 'app1/find.html',params)

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
            'title':'test',
            'msg':'ちゃんと挨拶したいので情報の登録をしてください',
            'form': Indexform(),
            'check_null_result':"未設定",
            'gopage':'secondindex'
        }

    def get(self,request):
        return render(request,'app1/index.html',self.params)

    def post(self,request):
        if ('check' in request.POST):
            self.params['checkresult']='何かがOK'
        else:
            self.params['checkresult']='何かがNG' #flag消しました

        if ('check_null' in request.POST):
            self.params['check_null_result']='何かがOK'
        else:
            self.params['check_null_result']='何かがNG' #flag消しました

        items = request.POST.getlist('choice_multiple')

        msg = 'こんにちは!'+request.POST['date']+'<br>'+request.POST['check']+'<br>'+request.POST['name']+'さん!<br>'+request.POST['area']+'にお住まいで<br>年齢は'+request.POST['age']+'歳<br>'+'メールアドレスは：'+ request.POST['mail']+'<br>URLは'+ request.POST['url'] +'<br>満足度:'+ items[0]+','+items[1]+ 'なんですね!<br>よろしくお願いします。'
        self.params["msg"] = msg
        self.params['form'] = Indexform(request.POST)
        return render(request,'app1/index.html',self.params)
