from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    bio = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to="profiles/")

    def save(self, *args, **kwargs):
        try:
            old_profile = Profile.objects.get(user=self.user)
            if old_profile:
                old_profile_image.delete(save=Fasle)
        except old_profile.DoesNotExist:
            pass
            super().save(*args, **args)

        def __str__(self):
            return f"{self.name} Profile"
