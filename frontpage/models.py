from django.db import models

class Vote(models.Model):
    ip_address = models.CharField(max_length=100)
    candidate = models.CharField(max_length=100)
    voted_at = models.DateTimeField(auto_now_add=True)

def __str__(self):
    return f"IP {self.ip_address} voted for {self.candidate}"