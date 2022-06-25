from django.contrib import admin
from .models import Comment,Section,Sub_section,Contact,Meeting

# Register your models here.


admin.site.register(Comment)
admin.site.register(Section)
admin.site.register(Sub_section)
admin.site.register(Contact)
admin.site.register(Meeting)