from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='list'),
    path('edit_bucket/<str:pk>/', views.editBucket, name='edit_bucket'),
    path('confirmDel/<str:pk>/', views.deleteBucket, name='confirmDel')
]