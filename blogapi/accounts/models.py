from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)  # User biography (optional)
    profile_image = models.ImageField(
        upload_to="profile_images/", blank=True, null=True
    )  # Profile picture
    is_author = models.BooleanField(
        default=False
    )  # Flag to mark if user is a blog author

    def __str__(self):
        return self.username
