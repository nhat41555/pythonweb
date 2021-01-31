from django.db import models

# Create your models here.
class Patient(models.Model):
    fullname = models.CharField(max_length=40)
    age = models.IntegerField(default=0)
    diagnostic = models.CharField(max_length=40)
    anamnesis = models.CharField(max_length=40)
    # image = models.ImageField(null=True,blank=True, upload_to="None")
    def __str__(self):
        s = "Họ tên là: " + str(self.fullname) + ", Tuổi là: " + str(self.age) + " Chuẩn đoán: " + str(self.diagnostic) + " Tiền sử bệnh: " + str(self.anamnesis)
        return s
