from django.db import models


class Campaign(models.Model):
    PLATFORM_CHOICES = [
        ('google', 'Google'),
        ('reddit', 'Reddit'),
        ('quora', 'Quora'),
    ]

    name = models.CharField(max_length=255)
    platform = models.CharField(max_length=20, choices=PLATFORM_CHOICES)
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    clicks = models.PositiveIntegerField(default=0)
    impressions = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
