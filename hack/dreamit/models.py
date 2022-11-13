from django.db import models

# Create your models here.
class Course(models.Model):
    cou_id = models.AutoField(primary_key=True),
    cou_title = models.CharField(max_length=100, default="")
    desc = models.CharField(max_length=100, default="")
    image = models.ImageField(upload_to="dreamit/image", default="")
    time = models.TimeField()

    def __str__(self):
        return self.cou_title

class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=70)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=500)

    def __str__(self):
        return self.name