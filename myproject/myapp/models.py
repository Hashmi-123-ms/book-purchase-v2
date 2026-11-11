from django.db import models

# Create your models here.


# class book(models.Model):
#     name=models.CharField(max_length=20)
#     age=models.IntegerField()
#     division=models.CharField(max_length=20)
#     place=models.CharField(max_length=20)
#     pdf=models.FileField(upload_to="pdf/",default="defualt.pdf")
#     cover=models.ImageField(upload_to="image/",blank=True)

class book(models.Model):
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    price=models.IntegerField()
    pdf=models.FileField(upload_to="pdf/",default="default.pdf")
    cover=models.ImageField(upload_to="image/",blank=True)

    
    def __str__(self):
        return self.title