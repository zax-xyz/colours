from django.contrib import admin

from .models import CeleryTask, Channel, Message, User

# Register your models here.
admin.site.register(CeleryTask)
admin.site.register(Channel)
admin.site.register(Message)
admin.site.register(User)
