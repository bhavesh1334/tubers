from django.contrib import admin
from .models import Hiretuber

# Register your models here.
class HAdmin(admin.ModelAdmin):
    list_display = ('first_name','email','tuber_name')
    list_display_links = ('first_name',)

admin.site.register(Hiretuber,HAdmin)