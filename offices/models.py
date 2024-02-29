from django.db import models

from users.models import BaseModel, User


class Office(BaseModel):
    floor = models.PositiveIntegerField(default=0)
    number = models.PositiveIntegerField(default=0)

    class Meta:
        indexes = [
            models.Index(fields=["floor"]),
            models.Index(fields=["floor", "number"]),
        ]

    def __str__(self):
        return f"{self.floor} | {self.number}"


class UserOffice(BaseModel):
    office = models.ForeignKey(Office, on_delete=models.PROTECT, related_name="office")
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_offices"
    )

    def __str__(self):
        return f"{self.office}: {self.user}"
