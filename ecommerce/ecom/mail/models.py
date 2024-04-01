from django.db import models

# Create your models here.
class Mail(models.Model):
    address = models.EmailField()
    title = models.CharField(max_length=32)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"the message was sent to {self.address}\
            at {self.timestamp} with title {self.title}\
            containing such message {self.message}"