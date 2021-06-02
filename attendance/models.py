from django.db import models
from employee.models import Employee


class Attendance(models.Model):
    empID = models.ForeignKey(
        Employee, on_delete=models.CASCADE, to_field='empID', db_constraint=False)
    daydate = models.DateField(auto_now_add=True)
    # daydate = models.DateField()
    timing_in = models.CharField(max_length=12, default="")
    timing_out = models.CharField(max_length=12, default="")
    status = models.CharField(max_length=2)


def __str__(self):
    return "{} -{}".format(self.empID, self.daydate)
