from django.contrib import admin
from django.contrib.auth.models import Group

admin.site.site_header = "BackendMS"
admin.site.site_title = "BMS"
admin.site.index_title = "Administration"

admin.site.unregister(Group)