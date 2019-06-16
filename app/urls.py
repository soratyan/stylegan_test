from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    # path("",views.IndexTemplateView.as_view(),name="index"),
    path("",views.index,name="index"),
    path("second", views.second, name='secondindex'),
    path("form",views.form, name='form'),
    path('create', views.create,name="create"),
    path('edit/<int:number>', views.edit,name="edit"),
    path('delete/<int:number>', views.delete,name="delete"),
    path('find', views.find,name="find"),
]
