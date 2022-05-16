from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('list', views.viewlist, name='list'),
    path('detail/<int:id>', views.detailview, name = 'detail'),
    path('delete/<int:id>', views.viewdelete, name = 'delete'),
    path('update/<int:id>', views.viewupdate, name = 'update'),
    path('create', views.viewcreate, name= 'create'),
    
    path('createtype', views.viewcreatetype, name= 'createtype'),
]