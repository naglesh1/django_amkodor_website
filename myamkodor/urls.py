from django.urls import path

from . import views

app_name = 'amkodor'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('general/', views.GeneralView.as_view(), name='general')
]
