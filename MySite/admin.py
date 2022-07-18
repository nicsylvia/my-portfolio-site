from django.contrib import admin
from MySite.models import *

# Register your models here.
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    prepopulated_field = {'slug': ('tittle', )}

admin.site.register(Message)
