from django.db import models

# Create your models here.
class Topic(models.Model):
    topic_name=models.CharField(primary_key=True,max_length=100)
    def __str__(self):
        return self.topic_name
class Webpage(models.Model):
    topic_name=models.ForeignKey(Topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    url=models.URLField()
    email=models.EmailField()
    mobile=models.CharField(default='9876543219')
    about=models.CharField(null=True,blank=True)
    def __str__(self):
        return self.name
class AccessRecord(models.Model):
    name=models.ForeignKey(Webpage,on_delete=models.CASCADE)
    author=models.CharField(max_length=100)
    date=models.DateField(auto_now_add=True)
