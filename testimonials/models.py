from django.db import models


class Testimonial(models.Model):
    buyer_name = models.CharField(max_length=100, null=False, blank=False)
    buyer_location = models.CharField(max_length=100, null=True, blank=True)
    review = models.TextField(max_length=1000, null=False, blank=False)
    image = models.ImageField(null=False, blank=False)

    def __str__(self):
        return self.buyer_name
