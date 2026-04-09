from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    bio = models.CharField(
        max_length=200,
    )
    image = models.ImageField(upload_to="profiles/", blank=True)

    def save(self, *args, **kwargs):
        try:
            old_profile = Profile.objects.get(user=self.user)
            if old_profile.image:
                old_profile.image.delete()
            super().save(*args, **kwargs)
        except Profile.DoesNotExist:
            super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}"
