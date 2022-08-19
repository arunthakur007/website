from django.contrib import admin
from .models import order
from.models import user
# Register your models here.

admin.site.register(order)
admin.site.register(user)