from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Profile)
admin.site.register(User_Withdraw)
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title',)
