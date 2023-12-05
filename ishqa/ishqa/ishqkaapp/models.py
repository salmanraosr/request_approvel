from django.db import models

# Create your models here.
class Request(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    mobile=models.IntegerField()
    aadhar=models.IntegerField()
    def __str__(self):
        return self.name
class Approved(models.Model):
    request = models.ForeignKey(Request, on_delete=models.CASCADE)
    approved_at= models.DateField(null=True, blank=True)

class Booking(models.Model):
    approved_at= models.ForeignKey(Approved, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=100,blank=True, null=True)
    country = models.CharField(max_length=100,blank=True, null=True)
    state = models.CharField(max_length=100,blank=True, null=True)
    city = models.CharField(max_length=100,blank=True, null=True)
    mobile=models.IntegerField(blank=True, null=True)
    aadhar=models.IntegerField(blank=True, null=True)
    days=models.IntegerField(blank=True, null=True)