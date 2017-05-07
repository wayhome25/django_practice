from django.core.urlresolvers import reverse
from django.db import models

class Bookmark(models.Model):
	title = models.CharField(max_length=100, blank=True)
	url = models.URLField('url', unique=True)

	def get_absolute_url(self):
		return reverse('bookmark:detail', args=[self.id])

	def __str__(self):
		return self.title
