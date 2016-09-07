from django.db import models

class GroupClass(models.Model):
	class_name = models.CharField(max_length=200)
	
	def __str__(self):
		return self.class_name


class Group(models.Model):
	group_class = models.ForeignKey(GroupClass, on_delete=models.CASCADE)
	group_name = models.CharField(max_length=200)

	def __str__(self):
		return self.group_name
