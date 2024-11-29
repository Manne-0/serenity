from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_created', 'summary', 'image')
    search_fields = ('title', 'content')
    list_filter = ('date_created',)

# Register the customized admin
admin.site.register(Post, PostAdmin)