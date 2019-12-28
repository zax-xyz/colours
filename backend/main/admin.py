from django.contrib import admin

from .models import CeleryTask, Channel, Message, User

# Register your models here.
class ChannelInline(admin.TabularInline):
    model = Channel.users.through


class ChannelAdmin(admin.ModelAdmin):
    model = Channel
    filter_horizontal = ('users',)


class UserAdmin(admin.ModelAdmin):
    exclude = ('password',)
    inlines = [ChannelInline]


admin.site.register(CeleryTask)
admin.site.register(Channel, ChannelAdmin)
admin.site.register(Message)
admin.site.register(User, UserAdmin)
