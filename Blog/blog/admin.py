from django.contrib import admin
from .models import CreateBlog,Comments
# Register your models here.

admin.site.register(CreateBlog)
admin.site.register(Comments)