from django.contrib import admin
from .models import Member, EditableContent

# Register your models here.

class MemberAdmin(admin.ModelAdmin):
  list_display = ("firstname", "lastname",)

@admin.register(EditableContent)
class EditableContentAdmin(admin.ModelAdmin):
    # Campos que se mostrarán en la lista
    list_display = ('pk', 'title', 'content', 'image', 'created_by')
    search_fields = ('title',)  # Campos en los que se puede buscar

admin.site.register(Member, MemberAdmin)

