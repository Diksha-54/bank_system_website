
from django.urls import path,include
from . import views
from django.conf.urls.static import *

urlpatterns = [
    path('',views.index,name="index"),
    path('viewall',views.viewall,name="viewall"),
    path('transfer',views.transfer,name="transfer"),
    path('transaction',views.transaction,name="transaction"),
]
