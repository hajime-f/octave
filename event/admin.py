from .models import Event
from django.contrib import admin
from django.utils.translation import gettext_lazy as _

class EventAdmin(admin.ModelAdmin):

    fieldsets = (
        (_('Event info'), {'fields': ('title', 'content', 'orchestra')}),
    )
    list_display = ('title', 'content', 'orchestra_name',)
    search_fields = ('title', 'content', 'orchestra',)
    ordering = ('created_at',)
    
    def orchestra_name(self, obj):
        return obj.orchestra.orchestra_name
    orchestra_name.short_description = '楽団名'
    
admin.site.register(Event, EventAdmin)
