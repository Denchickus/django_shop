from django.urls import path
#from myapp.views import index
from myapp.views import index, indexItem

app_name = 'myapp'

urlpatterns = [
    path('', index),
    path('<int:id>/', indexItem, name='detail'),
    
]