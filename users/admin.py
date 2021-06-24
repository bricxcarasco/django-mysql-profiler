from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from .models import User, Comment

# Register your models here.
admin.site.site_header = 'Profiler Admin'
admin.site.site_title = 'Profiler Admin'
admin.site.index_title = 'Welcome to the Profiler Administration'

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0

class UserAdmin(admin.ModelAdmin):
    list_display = ('image_tag', 'first_name', 'last_name', 'email', 'position')
    search_fields = ('first_name', 'last_name', 'email', 'position')
    inlines = [CommentInline]

class CommentAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'name', 'body', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('email', 'name', 'body')
    actions = ['approve_comment']

    def approve_comment(self, request, queryset):
        queryset.update(status=True)

admin.site.register(User, UserAdmin)
admin.site.register(Comment, CommentAdmin)
