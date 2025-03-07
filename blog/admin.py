from django.contrib import admin
from .models import Post, Moment, MomentMedia

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_created', 'summary', 'image', 'song_title')  # Show song_title in the list view
    search_fields = ('title', 'content', 'song_title')  # Allow searching by song_title
    list_filter = ('date_created',)
    fields = ('title', 'content', 'summary', 'image', 'youtube_link', 'song_title', 'song_message')  # Add fields for the form

class MomentMediaInline(admin.TabularInline):
    model = MomentMedia
    extra = 1  # Number of empty forms to display for adding media

@admin.register(Moment)
class MomentAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_created', 'category')
    inlines = [MomentMediaInline]

# Register the customized admin
admin.site.register(Post, PostAdmin)