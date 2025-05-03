from django.db import models

# Create your models here.
class PageVisit(models.Model):
    """Store information like visted webpages and timing"""

    # db -> table
    # id -> Hidden -> primary key -> autofield -> 1, 2, 3, ...
    path = models.TextField(blank=True, null=True) # col
    timestamp = models.DateTimeField(auto_now_add=True) # col
