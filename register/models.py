from django.db import models

class Users(models.Model):
    users_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=30, verbose_name='Name')
    user_surname = models.CharField(max_length=30, verbose_name='Surname')
    phone_number = models.CharField(max_length=13, verbose_name='Phone number')
    email = models.EmailField(max_length=100, verbose_name='Email')  # EmailField bilan almashtirildi
    company = models.CharField(max_length=100, verbose_name='Company')
    
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]
    
    gender = models.CharField(choices=GENDER_CHOICES, max_length=6, verbose_name='Gender')  # Max_length 6, chunki 'Female' 6 ta belgidan iborat
    
    class Meta:
        db_table = "Users"  # Agar siz aynan shu jadval nomidan foydalanmoqchi bo'lsangiz
        managed = True  # Modelni Django migration'lari orqali boshqarish
        
    def __str__(self) -> str:
        return f"{self.user_name} {self.user_surname}"
