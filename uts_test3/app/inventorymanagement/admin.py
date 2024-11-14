from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Admin)
admin.site.register(Category)
admin.site.register(Supplier)
admin.site.register(Item)