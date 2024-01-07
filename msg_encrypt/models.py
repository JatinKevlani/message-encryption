from django.db import models

# Create your models here.    
class Message(models.Model):
    message = models.TextField()
    encryption = models.TextField()
    password = models.CharField(max_length = 50)
    one_time_use = models.BooleanField()
    
    # To change the name of row view with a column value instead of object
    def __str__(self):
        return self.encryption