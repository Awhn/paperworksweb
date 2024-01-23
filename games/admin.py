from django.contrib import admin
from .models import GameContents, Comments

class GameContentsAdmin(admin.ModelAdmin):
    list_display = ['title', 'tags', 'thumbnail', 'published_at']
    search_fields = ['title']

class CommentsAdmin(admin.ModelAdmin):
    list_display = ['author', 'content_list', 'content', 'rating', 'create_date', 'modify_date']
    search_fields = ['author']

admin.site.register(GameContents, GameContentsAdmin)
admin.site.register(Comments, CommentsAdmin)
