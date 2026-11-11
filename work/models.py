from django.db import models
from accounts.models import User


class Category(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()

    def __str__(self):
        return self.name

class Course(models.Model):
    author_id = models.ForeignKey(User,on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    description=models.TextField()
    price=models.DecimalField(decimal_places=2,max_digits=7)
    is_published = models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Lesson(models.Model):
    course_id = models.ForeignKey(Course,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    video_url=models.CharField(max_length=300)
    content=models.TextField()
    order=models.IntegerField()
    created_at=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title
    

class Task(models.Model):

    UNUM = [
        ('lesson',"Lesson"),
        ('exam','Exam')
    ]
    

    lesson_id = models.ForeignKey(Course,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    description=models.TextField()
    task_type=models.Field(max_length=20,choices=UNUM, default='lesson')
    created_at=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.title
    