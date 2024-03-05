from django.db.models.signals import post_save
from django.dispatch import receiver

from offices.models import Assignment, UserRequest
@receiver(post_save, sender=UserRequest)
def create_assignment(sender, instance, created, **kwargs):
    """
    Automatically creates an Assignment instance when a UserRequest object is created.
    """
    if created:
        # Assuming you have imported Assignment model and Worker model properly
        # Also assuming User model is defined for assigned_by
        assignment = Assignment.objects.create(
            request=instance,
            assigned_by=instance.submitted_by.user
        )
