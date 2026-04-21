from django.contrib.auth.models import User
from django.db import models
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    bio = models.CharField(
        max_length=200,
    )
    image = models.ImageField(
        upload_to="profiles/", default="profiles/images.png", blank=True
    )

    def save(self, *args, **kwargs):
        try:
            old_profile = Profile.objects.get(user=self.user)
            if old_profile.image and old_profile.image.name != "images.png":
                old_profile.image.delete(save=False)
        except Profile.DoesNotExist:
            pass
        super().save(*args, **kwargs)
        if self.image:
            img = Image.open(self.image.path)
            if img.height > 300 or img.width > 300:
                img.thumbnail((300, 300))
                img.save(self.image.path)

    def __str__(self):
        return f"{self.name}"
