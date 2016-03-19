from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from .models import Dish

def index(request):
    dish_json = serializers.serialize('json', Dish.objects.all())
    return  HttpResponse( dish_json, content_type="application/json")
    #JsonResponse({ "dishes": dish_json})
