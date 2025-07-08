from django.db import models
from django.contrib.auth import get_user_model
from datetime import date
from calendar import monthrange


class InstalmentRate(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    activation_date = models.DateField(blank=False, null=False)
    created_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    deactivated_at = models.DateField(blank=True,
                                      null=True)

    def __str__(self):
        return f"{self.amount} from {self.activation_date}"

    class Meta:
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=['activation_date']),
        ]

    def deactivate_at_month_end(self):
        today = date.today()
        last_day = monthrange(today.year, today.month)[1]
        self.deactivated_at = date(today.year, today.month, last_day)
        self.save()

    @classmethod
    def get_instalment_rate(cls, month=None):
        if month is None:
            # get current:
            # deactivate date is none or greater than or eql current date
            # activation date is less than or eql to today
            today = date.today()
            return cls.objects.filter(
                activation_date__lte=today
            ).filter(
                models.Q(deactivated_at__isnull=True) | models.Q(deactivated_at__gte=today)
            ).order_by('-activation_date').first()
        else:
            # get for that months
            pass
