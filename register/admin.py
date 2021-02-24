from django.contrib import admin
from .models import UserProfile, Feedback
# Register your models here.

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject','date',)
    search_fields = ('name', 'email',)
    date_hierarchy = 'date'

class UserAdmin(admin.ModelAdmin):
    list_display = ('user', 'email', 'id','created',)
    search_fields = ('name', 'email',)
    date_hierarchy = 'created'    
    
admin.site.register(UserProfile, UserAdmin)
admin.site.register(Feedback, FeedbackAdmin)