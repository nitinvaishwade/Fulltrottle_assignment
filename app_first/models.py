from django.db import models

# Create your models here.




class sampleData(models.Model):
	"""
	sample data for operations
	"""
	name = models.CharField(max_length=20, blank=True, null=True)
	age = models.IntegerField(default=0)

	class Meta:
		db_table = 'sampledata'


