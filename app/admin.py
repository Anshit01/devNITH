from django.contrib import admin

from .models import Account, InternshipPost, OpenSourcePost

# Register your models here.
admin.site.register(Account)
admin.site.register(InternshipPost)
admin.site.register(OpenSourcePost)