from django.db import models
# Create your models here.

class Task(models.Model):
    name = models.CharField('タスク名', max_length=255)
    created_date = models.DateTimeField('作成日時', auto_now_add=True)
    update_date = models.DateTimeField('更新日時', auto_now=True)

    date = models.DateField()
    breakfast = models.BooleanField()


    def __str__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length=30)
    gender = models.BooleanField()
    age = models.IntegerField(default = 0)
    created_date = models.DateTimeField('作成日時', auto_now_add=True)
    update_date = models.DateTimeField('更新日時', auto_now=True)

    def __str__(self):
        return '<ID:'+str(self.id)+'>  名前:'+self.name+' ('+str(self.age)+'歳)'

class Touroku(models.Model):

    namelist = [
        ('妻','妻'),
        ('ひろゆき','ひろゆき'),
    ]

    status = [
        ('大変悪い','大変悪い'),
        ('悪い','悪い'),
        ('普通','普通'),
        ('良い','良い'),
        ('大変良い','大変良い'),
   ]

    date = models.DateField()
    name = models.CharField(max_length=30,choices = namelist)
    bf = models.BooleanField()
    lunch = models.BooleanField()
    dinner = models.BooleanField()
    eatout = models.BooleanField()
    drinking = models.BooleanField()
    workout = models.BooleanField()
    stretch = models.BooleanField()
    studying = models.BooleanField()
    awaketime = models.TimeField()
    asleeptime = models.TimeField()
    kenkobody = models.CharField(max_length=30,choices = status)
    workcond = models.CharField(max_length=30,choices = status)

    def __str__(self):
        return '<ID:'+str(self.id)+'>  名前:'+self.name+'/ 登録日：'+str(self.date)
