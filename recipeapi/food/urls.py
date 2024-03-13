"""
URL configuration for recipeapi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include
from food import views
from rest_framework.authtoken import views as rviews


urlpatterns = [
    path('all',views.ListAll.as_view()),
    # path('register',views.Register.as_view()),
    path('api-token-auth',rviews.obtain_auth_token),
    path('review',views.Rate_review.as_view()),
    # path('all/<str:pk>',views.SpecificRecipe.as_view()),

]
