from django.contrib import admin
from .models import Post, Offers
from django_summernote.admin import SummernoteModelAdmin

class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('text',)


admin.site.register(Post, PostAdmin)
admin.site.register(Offers)