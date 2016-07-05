from django.db import models

# Create your models here.
class Site( models.Model ):
	title = models.CharField( max_length=200 )

	def __str__( self ): # __unicode__ on Python 2
		return self.title
	def accumulate( self, key ):
		return key

class Site_value( models.Model ):
	#Many-to-one relationships
	site_name = models.ForeignKey( Site, on_delete=models.CASCADE, verbose_name='Site' )
	
	date = models.DateField( verbose_name='Date')
	A_value = models.DecimalField( max_digits=5, decimal_places=2, verbose_name='A Value' )
	B_value = models.DecimalField( max_digits=5, decimal_places=2, verbose_name='B Value' )

	def __str__( self ):  #__unicode__ on Python 2
		return str( self.date )
