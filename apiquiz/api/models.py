from django.db import models

# Create your models here.

class Quiz(models.Model):
    Subject=models.CharField(blank=False,max_length=100)
    StartTime=models.DateTimeField()
    EndTime=models.DateTimeField()

    def __str__(self):
        return self.Subject

class Questions(models.Model):
    sub=models.ForeignKey(Quiz,blank=True,on_delete=models.CASCADE,related_name="questions")
    subquestions=models.CharField(max_length=2000)

    def __str__(self):
        return self.subquestions

class Answer(models.Model):
    Que = models.ForeignKey(Questions,blank=False,on_delete=models.CASCADE,related_name="options")
    Option=models.CharField(max_length=1000)
    righ=models.BooleanField(default=False)

    def __str__(self):
        return self.Option


