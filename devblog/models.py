from django.db import models

class Post(models.Model):
    date = models.DateField(auto_now=True)
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    text = models.TextField()

    def __str__(self) -> str:
        return f"{self.author} - {self.title}"