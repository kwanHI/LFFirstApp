from django.db import models
from django.utils import timezone

# Create your models here.

class Register(models.Model):
	client = models.ForeignKey('auth.User')
	programService = models.CharField(max_length=200)
	programNote    = models.TextField()
	created_date   = models.DateTimeField(
		                    default=timezone.now)
	published_date = models.DateTimeField(
		                    blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()


	def __str__(self):
		return self.programService
