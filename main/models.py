from django.db import models

# Create your models here.
class ToDoList(models.Model):
    first_name = models.CharField(max_length=50, blank=True)  # Add "{name}"'s before To-do List else blank
    items = models.JSONField()
    submitted_at = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    is_flagged = models.BooleanField(default=False)  # Moderate the sociopaths

    # possible over engineering:
    # Add a likes counter to lists people find funny/useful
    # Tag lists as serious/funny/shitpost
    # Add an RSS feed: “Latest 10 Public Lists”
    # Add a /leaderboard of the most liked lists
    # Add scheduled cleanup of old or inactive lists
