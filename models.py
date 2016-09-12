from django.db import models

class GroupInfo(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	group_name = models.CharField(max_length=100)
	class_name = models.CharField(max_length=100)

	def __str__(self):
		return (self.first_name + " " + self.last_name + " | " + self.group_name + " | " + self.class_name)
