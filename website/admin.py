from django.contrib import admin

from website.models import BlogArticles


# Register your models here.

@admin.register(BlogArticles)
class Articles(admin.ModelAdmin):
    list_display = ("title", "date", "publish")
    list_editable = ("title", )
    list_display_links = ("date", )
    search_fields = ("title" ,)
    list_filter = ("date" ,)
    list_per_page =25
