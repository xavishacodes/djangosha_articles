"""djangoblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('',views.article_list, name="list"),
    # path('(?P<slug>[\w-]+)/', views.article_details),\
    path('create/', views.article_create, name="create"),
    path('<slug:slug>/', views.article_details, name="details"),
    #here the above line, the slug is defined as a named capturing group.
]
