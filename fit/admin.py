from django.contrib import admin

# Register your models here.

from .models import Restaurant, Diet, Dish, User

admin.site.register(Restaurant)
admin.site.register(Diet)
admin.site.register(Dish)
admin.site.register(User)