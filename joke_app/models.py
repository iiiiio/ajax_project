from django.db import models


# to display an object in the Django admin site and as
# the value inserted into a template when it displays an object
class Joke(models.Model):
    joke_title = models.CharField(max_length=200)
    joke = models.TextField(default='')
    answer = models.TextField(default='')

    def __str__(self):
        return self.joke_title
