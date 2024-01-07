from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from . import models


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category','author', 'create_at']
    exclude = ['slug']
    save_as = True
    save_on_top = True


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'message', 'author', 'post']


admin.site.register(models.Category, MPTTModelAdmin)
admin.site.register(models.Tag)

