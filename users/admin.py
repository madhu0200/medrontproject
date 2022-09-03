from django.contrib import admin
from .models import CustomUser,mobiles,otp
# Register your models here.
admin.site.register(CustomUser)
admin.site.register(mobiles)
admin.site.register(otp)