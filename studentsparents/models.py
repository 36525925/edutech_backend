from django.db import models
from parents.models import Parents
from students.models import Students

class StudentsParents(models.Model):
        parentID = models.ForeignKey(Parents, on_delete=models.CASCADE)
        studentID = models.ForeignKey(Students, on_delete=models.CASCADE)
        parentType_choices = [
            ('Mother', 'Mother'),
            ('Father', 'Father'),
            ('Guardian', 'Guardian'),
            ('Sponsor', 'Sponsor'),
        ]
        parentType = models.CharField(max_length=8, choices=parentType_choices)
        dateCreated = models.DateField(auto_now_add=True)

        def __str__(self):
            return f"{self.parentID.parentName} - {self.studentID.studentName}"


class Meta:
    db_table = 'studentsparents'  # Optional: specify the database table name

