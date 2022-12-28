from django.db import models

# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length = 200)
    complete = models.BooleanField(default = False)
    created = models.DateTimeField(auto_now_add = True)
    link = models.URLField(max_length = 200, default="https://www.google.com/webhp?hl=en&ictx=2&sa=X&ved=0ahUKEwjrhov_gZ38AhXAD1kFHdEvCbcQPQgJ")

    def __str__(self):
        return self.title
