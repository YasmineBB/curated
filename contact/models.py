from django.db import models


class ContactForm(models.Model):
    contact_name = models.CharField(max_length=100, null=False, blank=False)
    contact_email = models.EmailField(max_length=100, null=False, blank=False)
    contact_subject = models.CharField(max_length=100, null=True, blank=True)
    contact_message = models.TextField(
        max_length=1000, null=False, blank=False
        )
    date = models.DateTimeField(auto_now_add=True)
    have_replied = models.BooleanField(default=False)

    def __str__(self):
        return self.contact_email

    class Meta:
        ordering = ['-date']
