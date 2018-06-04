from django.db import models

# Create your models here.
class Makanan(models.Model):
	nama_makanan = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')

	def __str__(self):
		return self.nama_makanan

	def was_published_recently(self):
		return self.pub_date >= (timezone.now()) - datetime.delta(days=1)

class Minuman(models.Model):
	makanan = models.ForeignKey(Makanan, on_delete = models.CASCADE)
	nama_minuman = models.CharField(max_length = 200)
	votes = models.IntegerField(default=0)

	def __str__(self):
		return self.nama_minuman
