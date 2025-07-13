from django.contrib import admin
from .models import Post


# Register the Post model with custom admin options to improve usability
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # Columns to display on the post list page in the admin
    list_display = ("title", "author", "created_at", "updated_at")

    # Enable search box for these fields (allows searching posts by title, body, or author's username)
    search_fields = ("title", "body", "author__username")

    # Add filters on the sidebar to filter posts by creation and update dates
    list_filter = ("created_at", "updated_at")
