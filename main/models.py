from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Career(models.Model):
  applicant = models.ForeignKey(User, default=None, blank=True, on_delete=models.SET_NULL, null=True)
  name = models.CharField(max_length=255)
  type = models.CharField(max_length=255, default = "TBD")
  package = models.IntegerField()
  location = models.CharField(max_length=255, default = "TBD")
  description = models.CharField(max_length=1024)
  image_url = models.CharField(max_length=512)

  def __str__(self):
    return self.name