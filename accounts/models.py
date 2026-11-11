from django.db import models

class User(models.Model):
    UNUM = [
        ('student',"Student"),
        ('author','Author'),
        ('admin','Admin')
    ]
    email=models.EmailField(max_length=200)
    password=models.CharField(max_length=200)
    full_name=models.CharField(max_length=100)
    role=models.Field(max_length=20,choices=UNUM, default='student')
    created_at=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name

