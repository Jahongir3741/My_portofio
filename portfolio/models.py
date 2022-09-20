from django.db import models


class Author(models.Model):
  first_name=models.CharField(max_length=256)
  last_name=models.CharField(max_length=256)
  birthday=models.DateField()
  image_url=models.ImageField(upload_to='img',null=True,blank=True)
  phone_number=models.CharField(max_length=13)
  email=models.EmailField(max_length=128,unique=True)
  city=models.CharField(max_length=256)

  def __str__(self):
    return self.first_name
  


class Networks(models.Model):
  network_link=models.URLField(max_length=256)
  icon=models.CharField(max_length=64)

  def __str__(self) -> str:
    return self.icon



class Contact(models.Model):
  your_name=models.CharField(max_length=512)
  your_email=models.EmailField(max_length=128,unique=True)
  subject=models.CharField(max_length=512)
  message=models.TextField()
  created=models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.your_name



class Skills(models.Model):
  name=models.CharField(max_length=256)
  prasent=models.IntegerField(default=0)
  color=models.CharField(max_length=512)

  def __str__(self):
    return self.name
  

class Resume(models.Model):
  resumes=models.CharField(max_length=256)
  title=models.CharField(max_length=256)
  r_date=models.CharField(max_length=128)
  region=models.CharField(max_length=256)

  def __str__(self) -> str:
    return self.resumes


class Text(models.Model):
  desc=models.TextField()

  def __str__(self) -> str:
    return self.desc[:100]



