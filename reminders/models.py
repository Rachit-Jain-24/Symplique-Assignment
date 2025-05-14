from django.db import models

class Reminder(models.Model):
    REMINDER_TYPES = [
        ('email', 'Email'),
        ('sms', 'SMS'),
    ]

    message = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    reminder_type = models.CharField(max_length=10, choices=REMINDER_TYPES)

    def __str__(self):
        return f"{self.message} at {self.date} {self.time} via {self.reminder_type}"
