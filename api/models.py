from django.db import models

class profile(models.Model):

    first_name=models.CharField(max_length=100)
    second_name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100,unique=True)
    mobile=models.CharField(max_length=13,unique=True)


    def __str__(self):
        return self.email

    class Meta:
        #db_table = ''
        managed = True
        verbose_name = 'profile'
        verbose_name_plural = 'profiles'
