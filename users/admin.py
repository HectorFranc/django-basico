# Django
from django.contrib import admin

# Models
from users.models import Profile

# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    "Profile admin."

    list_display = ('pk', 'user', 'phone_number', 'website', 'picture')
    list_display_links = ('pk', 'user')
    list_editable = ('phone_number', 'website', 'picture')
    list_filter = (
        'user__is_active',
        'user__is_staff',
        'created',
        'updated',
    )

    search_fields = (
        'user__email',
        'user__username',
        'user__first_name',
        'user__last_name',
        'phone_number'
    )
    fieldsets = (
        ('Profile', {
            'fields': ('user', 'picture')
        }),
        ('Extra info', {
            'fields': (
                ('website', 'phone_number'),
                ('biography', )
            )
        }),
        ('Metadata', {
            'fields': (
                ('created', 'updated'),
            )
        })
    )
    read_only_fields = ('created', 'updated', 'user')
