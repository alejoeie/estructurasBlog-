from django.contrib import admin

# Register your models here.
from .models import Home, Subscribers, Contact


admin.site.register(Home)
admin.site.register(Subscribers)
admin.site.register(Contact)