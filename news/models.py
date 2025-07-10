from django.db import models

class New(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='news')
    content = models.TextField()

    def __str__(self):
        return self.title
    
