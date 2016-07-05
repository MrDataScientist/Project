from django.contrib import admin
from .models import Site, Site_value

class SiteAdmin(admin.ModelAdmin):
    #List Display for SiteAdmin
    list_display = ( 'title', )

class Site_valueAdmin(admin.ModelAdmin):
    #Values List Display for Site_valueAdmin
    list_display = ( 'site_name', 'A_value', 'B_value', 'date' )
	
	# Register your models here.
admin.site.register( Site, SiteAdmin)
admin.site.register( Site_value, Site_valueAdmin)