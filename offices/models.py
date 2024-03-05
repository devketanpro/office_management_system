from django.db import models
from django.core.validators import MinValueValidator
from django.utils import timezone
from users.models import BaseModel, User, Worker


class STATUS(models.IntegerChoices):
    PENDING = 1, "Pending"
    SCHEDULED = 2, "Scheduled"
    IN_PROGRESS = 3, "In Progress"
    COMPLETED = 4, "Completed"
    DELAYED = 5, "Delayed"
    FAILED = 6, "Failed"
    UPDATED = 7, "Updated"
    CANCELLED = 8, "Cancelled"


class REQUEST_TYPE(models.IntegerChoices):
    CLEAN = 1, "Clean"
    COMPLAINT = 2, "Complaint"
    PROBLEM = 3, "Problem"
    REQUEST = 4, "Request"
    ADDITION = 5, "Addition"
    REMOVE = 6, "Remove"


class TIME_RANGE(models.IntegerChoices):
    FIRST = 1, "8-10"
    SECOND = 2, "10-12"
    THIRD = 3, "12-2"
    FOURTH = 4, "2-4"
    OTHER = 5, "Other"


class PRIORITY(models.IntegerChoices):
    LOW = 1, "Low"
    MEDIUM = 2, "Medium"
    HIGH = 3, "High"
    URGENT = 4, "Urgent"


class Office(BaseModel):
    """
    Represents an office location in a building.
    """

    building = models.CharField(max_length=25)
    floor = models.PositiveIntegerField(
        validators=[MinValueValidator(1)],
    )
    office_number = models.PositiveIntegerField(validators=[MinValueValidator(1)])

    class Meta:
        unique_together = ["building", "floor", "office_number"]
        indexes = [
            models.Index(fields=["building"]),
            models.Index(fields=["building", "floor"]),
            models.Index(fields=["building", "floor", "office_number"]),
        ]

    def __str__(self):
        """
        Return a string representation of the office location.
        """

        return f"{self.building} | {self.floor} | {self.office_number}"


class UserOffice(BaseModel):
    """
    Represents a user's association with an office location.
    """

    office = models.OneToOneField(
        Office, on_delete=models.CASCADE, limit_choices_to={"useroffice__isnull": True}
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="user_office",
        limit_choices_to={"role": 2},
    )

    def __str__(self):
        """
        Return a string representation of the user's association with the office.
        """

        return f"{self.office}: {self.user}"


class UserRequest(BaseModel):
    """
    Represents a user request submitted to the system.
    """

    request_type = models.IntegerField(
        choices=REQUEST_TYPE.choices, default=REQUEST_TYPE.CLEAN
    )
    title = models.CharField(max_length=255, blank=True)
    preferred_timeframe = models.IntegerField(
        choices=TIME_RANGE.choices, default=TIME_RANGE.FOURTH
    )
    submitted_by = models.ForeignKey(UserOffice, on_delete=models.CASCADE)

    class Meta:
        unique_together = ["request_type", "submitted_by"]
        indexes = [
            models.Index(fields=["request_type"]),
        ]

    def __str__(self):
        """
        Return a string representation of the user request.

        Returns:
            str: A formatted string containing information about the request.
        """
        return f"{self.submitted_by}: {self.title}"


class Assignment(BaseModel):
    """
    Represents an assignment of a user request to a worker.
    """

    request = models.OneToOneField(
        UserRequest,
        on_delete=models.CASCADE,
        limit_choices_to={"assignment__isnull": True},
    )
    worker = models.ForeignKey(
        Worker,
        on_delete=models.CASCADE,
        related_name="user_request",
        null=True,
        limit_choices_to={"is_busy": False},
    )
    priority = models.IntegerField(
        choices=PRIORITY.choices, default=PRIORITY.LOW
    )
    status = models.IntegerField(
        choices=STATUS.choices, default=STATUS.PENDING
    )
    last_update = models.DateTimeField(default=timezone.now)
    assigned_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    class Meta:
        indexes = [
            models.Index(fields=["priority"]),
            models.Index(fields=["status"]),
        ]

    def __str__(self):
        """
        Return a string representation of the assignment.

        Returns:
            str: A formatted string containing information about the assignment.
        """
        return f"request_id:- {self.request.id} | status:- {self.status} | priority:- {self.priority}"

    def save(self, *args, **kwargs):
        """
        Save the assignment and mark the assigned worker as busy.

        Overrides the default save method to update the status of the assigned worker.
        """

        if self.worker:
            self.worker.is_busy = True
            self.worker.save()
        super().save(*args, **kwargs)
