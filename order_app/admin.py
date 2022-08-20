from django.contrib import admin
from .models import Order
from .models import Profile
from .models import user_information
from .models import store_information
from .models import store_item
# Register your models here.

admin.site.register(Order)
admin.site.register(Profile)
admin.site.register(user_information)
admin.site.register(store_information)
admin.site.register(store_item)

