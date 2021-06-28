
from django.urls import path

from . import views
urlpatterns = [
    path('', views.blogslist, name='blogslist'),
    path('<int:blog_id>', views.detail, name='detail'),
]
