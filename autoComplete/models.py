from django.db import models

# Create your models here.
class words(models.Model):
    word = models.CharField(max_length=20)
    
    def __unicode__(self):
        return self.word
    
    def tellCount(self):
        return self.objects.filter(word="testCaseNow").count()