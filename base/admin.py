from django.contrib import admin
from .models import Room , Topic, Message


class TopicAdmin(admin.ModelAdmin):
    list_display=("id","name")
    ordering=['id']


class RoomAdmin(admin.ModelAdmin):
    list_display=("id","host","name","description","created","updated")
    ordering=['id']


class MessageAdmin(admin.ModelAdmin):
    list_display=("id","user","body","created","updated")
    ordering = ['id']


admin.site.register(Topic,TopicAdmin)
admin.site.register(Room,RoomAdmin)
admin.site.register(Message,MessageAdmin)