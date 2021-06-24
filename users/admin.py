from django.contrib import admin
from .models import User

# Register your models here.
admin.site.site_header = 'Profiler Admin'
admin.site.site_title = 'Profiler Admin'
admin.site.index_title = 'Welcome to the Profiler Administration'

class UserAdmin(admin.ModelAdmin):
    list_display = ['image_tag', 'first_name', 'last_name', 'email', 'position']
    search_fields = ['first_name', 'last_name', 'email', 'position']

admin.site.register(User, UserAdmin)
