from django.db.models import Avg, Sum
from django.shortcuts import render
from django.views import generic
from .models import Site

# Create your views here.
class Index( generic.ListView ):
	template_name = 'myapp/index.html'
	def get_queryset( self ):
		return Site.objects.all()

class detail( generic.DetailView ):
	template_name = 'myapp/site_details.html'
	model = Site

class Sum_value( generic.ListView ):
	template_name = 'myapp/summary.html'
	def get_queryset( self ):
		return Site.objects.annotate( sum_A_value= Sum( 'site_value__A_value' ), sum_B_value= Sum( 'site_value__B_value' ) )
"""
Averages via Raw SQL
"""
class Average( generic.ListView ):
	template_name = 'myapp/summary.html'
	def get_queryset( self ):
		sql_query = 'SELECT site.*, ( SELECT AVG( A_value ) FROM myapp_site_value WHERE site_name_id=site.id ) AS sum_A_value, ( SELECT AVG( B_value ) FROM myapp_site_value WHERE site_name_id=site.id ) AS sum_B_value FROM myapp_site site'
		return Site.objects.raw( sql_query )