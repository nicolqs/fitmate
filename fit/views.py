from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from .models import Dish, Restaurant
import json


def dishes(request):
    dish_json = serializers.serialize('json', Dish.objects.all())
    return JsonResponse({ "dishes": json.loads(dish_json)})

def restaurants(request):
    restau_json = serializers.serialize('json', Restaurant.objects.all())
    return JsonResponse({ "restaurants": json.loads(restau_json)})

