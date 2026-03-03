from django.contrib import admin
from .models import Server
# Register your models here.
class ServerAdmin(admin.ModelAdmin):
    list_display = ['id','name','username','joinDate']

admin.site.register(Server, ServerAdmin)