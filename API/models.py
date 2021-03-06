from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())

class ideator(models.Model):
    created= models.DateTimeField(auto_now_add=True)
    name= models.CharField(max_length=50, blank=True, default='')
    email=models.CharField(max_length=50)
    title=models.CharField(max_length=50)
    description=models.CharField(max_length=100)


    def __str__(self):
         return (self.name)

    class Meta:
         ordering= ('created',)
