from django.contrib import admin
# Register your models here.

# Taskモデルをインポート
from .models import Task
from .models import User

# 管理サイトへのモデルを登録
admin.site.register(Task)
admin.site.register(User)
