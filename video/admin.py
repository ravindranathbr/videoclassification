from django.contrib import admin

# Register your models here.

from .models import Video

class VideoAdmin(admin.ModelAdmin):
    list_display = ('url', 'downloadStatus', 'testResult', 'typeOfProcesses', 'created_at') # Displays the list in index page
    fieldsets = [
        ('Enter video url',               {'fields': ['url']}),
        ('Type of Process', {'fields': ['typeOfProcesses'], 'classes': ['collapse']}),
    ]
    list_filter = ['created_at']
    search_fields = ['url']


# Pass VideoAdmin as second argument to the admin register
admin.site.register(Video, VideoAdmin)
