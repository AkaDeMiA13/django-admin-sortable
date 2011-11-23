from django.contrib import admin

from adminsortable.admin import SortableAdmin, SortableTabularInline, SortableStackedInline
from app.models import Category, Project, Credit, Note, Sample


admin.site.register(Category, SortableAdmin)


class CreditInline(SortableTabularInline):
    model = Credit


class NoteInline(SortableStackedInline):
    model = Note


class ProjectAdmin(SortableAdmin):
    inlines = [CreditInline, NoteInline]
    list_display = ['__unicode__', 'category']

admin.site.register(Project, ProjectAdmin)
admin.site.register(Sample, SortableAdmin)
