import uuid
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

from users.manager import CustomUserManager


class USER_TYPE(models.IntegerChoices):
    ADMIN = 1, "Admin"
    USER = 2, "User"
    WORKER = 3, "Worker"


class WORKER_TYPE(models.IntegerChoices):
    IT = 2, "IT"
    WORKER = 5, "Worker"
    CLEANER = 6, "Cleaner"
    OTHER = 7, "Other"


class BaseModel(models.Model):
    """
    Base model with common fields like ID, creation timestamp,
    and soft delete indicators.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    is_active = models.BooleanField(
        default=True, help_text="Indicates if the record is active."
    )
    is_deleted = models.BooleanField(
        default=False, help_text="Indicates if the record is deleted."
    )
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
        ordering = ["-created"]


class User(BaseModel, AbstractUser, PermissionsMixin):
    """
    Custom user model representing a user in the system.
    """

    username = None
    email = models.EmailField(_("email address"), unique=True)
    phone = models.CharField(max_length=25)
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    role = models.IntegerField(
        choices=USER_TYPE.choices, default=USER_TYPE.USER, help_text="User role."
    )

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        indexes = [
            models.Index(fields=["role"]),
        ]

    def __str__(self) -> str:
        """
        Returns a string representation of the user.

        If both first name and last name are available, it returns the full name.
        If the full name is not available but the phone number is, it returns the phone number.
        Otherwise, it returns the email address.

        Returns:
            str: String representation of the user.
        """
        return (
            f"{self.first_name} {self.last_name}".strip()
            if self.first_name and self.last_name
            else self.email
        )


class Worker(BaseModel):
    """
    Represents a worker in the system.
    """

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        limit_choices_to={"role": 3, "worker__isnull": True},
    )
    worker_type = models.IntegerField(
        choices=WORKER_TYPE.choices, default=WORKER_TYPE.OTHER
    )
    is_busy = models.BooleanField(default=False)

    class Meta:
        indexes = [
            models.Index(fields=["worker_type"]),
            models.Index(fields=["is_busy"]),
            models.Index(fields=["worker_type", "is_busy"]),
        ]

    def __str__(self):
        """
        Return a string representation of the worker.

        Returns:
            str: A formatted string containing information about the worker.
        """

        return f"{self.user}: {self.worker_type}"
