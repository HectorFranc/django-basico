# Django
from django.contrib import admin

# Models
from posts.models import Post

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Post admin."""
    fieldsets = (
        ('Post', {
            'fields': ('title', 'photo')
        }),
        ('User', {
            'fields': ('user', 'profile')
        }),
        ('Metadata', {
            'fields': ('created', 'updated')
        })
    )

    readonly_fields = ('created', 'updated')
