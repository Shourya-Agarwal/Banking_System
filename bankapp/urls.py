
from django.contrib import admin
from django.urls import path
from bankapp import views
urlpatterns = [
    path('',views.index, name='bankhome'),
    path('customers',views.customers,name='customers'),
    path('history',views.history,name="history"),
    path('transaction/',views.transaction,name="transaction"),
    path('update_info/',views.update_info,name="update_info"),
    path('this',views.this,name="this")
]
