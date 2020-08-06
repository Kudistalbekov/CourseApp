from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('',admin.site.urls),
    path('app/',CourseAPI.as_view(),name='list'),
    path('app/<int:id>/',CourseDetailAPI.as_view(),name='by_id')
]

'''
    path('category/',CategoryAPI.as_view()),
    path('category/<int:id>/',CategoryDetailAPI.as_view()),
    path('branch/',BranchAPI.as_view()),
    path('branch/<int:id>/',BranchDetailAPI.as_view()),
    path('contact/',ContactAPI.as_view()),
    path('contact/<int:id>/',ContactDetailAPI.as_view())
'''