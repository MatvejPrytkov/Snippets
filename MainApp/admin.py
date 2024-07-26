from django.contrib import admin
from MainApp.models import Snippet
#admin.site.register(Snippet)
# Register your models here.
@admin.register(Snippet)
class SnippetAdmin(admin.ModelAdmin):
    list_display = ["name", "lang", "creation_date", "code"]
    list_filter = ["lang", "creation_date"]
    ordering = ["creation_date"]
    search_fields = ["name", "code"]