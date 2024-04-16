from django.contrib import admin
from .models import Mavzu, UsersBot, Qism, Bolim
# Register your models here.


class MavzuAdmin(admin.ModelAdmin):
    list_display = ('savol', 'javob', 'created_at', 'qism', 'bolim')
    search_fields = ('savol',)


class UsersBotAdmin(admin.ModelAdmin):
    list_display = ('name', 'user_id', 'created')
    search_fields = ('name', 'user_id')


class QismAdmin(admin.ModelAdmin):
    list_display = ('name',)


class BolimAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Mavzu, MavzuAdmin)
admin.site.register(UsersBot, UsersBotAdmin)
admin.site.register(Qism, QismAdmin)
admin.site.register(Bolim, BolimAdmin)
