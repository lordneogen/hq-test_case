from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Product(models.Model):  
        
    name = models.TextField(null=False)
    
    author = models.ForeignKey(User,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return str(self.name)

    class Meta:

        managed = True
        db_table = 'product'
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        
class Product_users(models.Model):  
        
    product = models.ForeignKey(Product,null=False,on_delete=models.CASCADE)
    
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.product)+" "+str(self.user)

    class Meta:
        
        unique_together = (('product', 'user'),)
        
        managed = True
        db_table = 'product_users'
        verbose_name = 'Пользователь продукта'
        verbose_name_plural = 'Пользователи продукта'
        
class Product_lesson(models.Model):  
        
    name = models.TextField(null=False)
    
    url=models.TextField(null=False)
    
    time=models.IntegerField(null=False)
    
    product = models.ForeignKey(Product,null=False,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)+",Продукт: "+str(self.product)

    class Meta:
        
        unique_together = (('id', 'product'),)
        managed = True
        db_table = 'product_lessons'
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
        
class Lessons_status(models.Model):  
    
    class status_text(models.TextChoices):
        Viewed = "Просмотренно"
        Not_viewed = "Не просмотренно"

    lesson=models.ForeignKey(Product_lesson,null=False,on_delete=models.CASCADE)
    
    status=models.TextField(
        choices=status_text.choices,
        default=status_text.Not_viewed,
    )
    
    user=models.ForeignKey(User,null=False,on_delete=models.CASCADE)
    
    date=models.DateField(null=True)
    
    time=models.IntegerField(null=False)

    def __str__(self):
        return str(self.lesson)+",просмотр "+str(self.user)

    class Meta:
        
        unique_together = (('user', 'lesson'),)
        managed = True
        db_table = 'lessons_status'
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'
        


