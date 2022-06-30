from django.contrib import admin
from home.models import Contact, Projects

from django.utils.translation import gettext_lazy as _

admin.site.index_title = 'АДМИНИСТРАЦИЯ САЙТА'
admin.site.site_header = 'ORIGIN DIGITAL - Панель управления'
admin.site.site_title = 'Панель управления'


class ContactAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone', 'ip']
    readonly_fields = ['first_name', 'last_name', 'phone', 'message', 'create_time', 'create_date', 'ip']


class ProjectsAdmin(admin.ModelAdmin):
    list_display = ['title', 'site_link', 'image_tag']


admin.site.register(Projects, ProjectsAdmin)
admin.site.register(Contact, ContactAdmin)
