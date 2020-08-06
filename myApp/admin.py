from django.contrib import admin
from .models import Category,Course,Branch,Contact
# Register your models here.
admin.site.register(Category)
admin.site.register(Course)
admin.site.register(Branch)
admin.site.register(Contact)
