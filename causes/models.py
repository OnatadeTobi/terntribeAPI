from django.db import models

# Create your models here.
class Cause(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image_url = models.URLField()

    def __str__(self):
        return self.title

class Contribution(models.Model):
    cause = models.ForeignKey(Cause, on_delete=models.CASCADE, related_name='contributions')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.amount}"