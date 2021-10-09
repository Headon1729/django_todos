from django.contrib import admin
from app.models import Todo

# Register your models here.


class ToDoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'priority')
    list_editable = ['description']


admin.site.register(Todo, ToDoAdmin)
