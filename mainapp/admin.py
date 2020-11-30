from django.contrib import admin
from .models import users, groups, list_items, works
admin.site.register(users)
admin.site.register(groups)
admin.site.register(list_items)
admin.site.register(works)

# Register your models here.
