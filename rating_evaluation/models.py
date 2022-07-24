from django.db import models

# Create your models here.


class RatingEvaluate(models.Model):

    section = models.ForeignKey(
        "software.SoftwareSection",
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    software = models.ForeignKey(
        "software.Software",
        on_delete=models.CASCADE,
        blank=False,
        null=False
    )
    max = models.PositiveSmallIntegerField(blank=False, null=False)
    is_active = models.BooleanField(default=True)
    created_by = models.ForeignKey(
        "authentication.Account",
        on_delete=models.CASCADE,
        blank=False,
        null=False
    )
    created_datetime = models.DateTimeField(auto_now=True)
    modified_datetime = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.section in self.software.sections.all():
            pass
        else:
            if self.section == None:
                pass
            else:
                raise Exception(
                    "Selected section is not in sections of this software"
                )
        return super().save(*args, **kwargs)
