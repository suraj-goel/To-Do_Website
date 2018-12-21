from django.db import models

# Create your models here.
class List(models.Model):
	item = models.CharField(max_length=200)
	completed = models.BooleanField(default = False)


	def __str__(self):
		return self.item

# creating a database is a 3 step process 
# 1. create a class in models.py
# 2. makemigrations (contains the intermediate code to make database)
# 3. save the migrations or migrate (creating an actual dbtable corresponding to model)