from django.db import models

# Create your models here.
class Product(models.Model):
    x=[
        ('Electronics', 'Electronics'),
        ('Clothes', 'Clothes'),
        ('Books', 'Books'),
        ('Furniture', 'Furniture'),
    ]
    name = models.CharField(max_length=100)
    content = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='photos/%y/%m/%d', null=True, blank=True)
    active = models.BooleanField(default=True)
    category = models.CharField(max_length=50, null=True, blank=True, choices=x)
    def __str__(self):
         return self.name
    class Meta:
        ordering = ['name']

class Female(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
         return self.name

class Male(models.Model):
    name_male = models.CharField(max_length=100)
    girls= models.OneToOneField(Female, on_delete=models.CASCADE)
    
    def __str__(self):
            return self.name_male

class Order_Product(models.Model):
    title = models.CharField(max_length=100)
    def __str__(self):
        return self.title   

class User(models.Model):
    name_user= models.CharField(max_length=100)
    product = models.ForeignKey(Order_Product, on_delete=models.CASCADE)

    def __str__(self):
            return self.name_user        

class Video(models.Model):
    title = models.CharField(max_length=100)
    def __str__(self):
        return self.title   

class User_Video(models.Model):
    name_user= models.CharField(max_length=100)
    watch = models.ManyToManyField(Video, blank=True)

    def __str__(self):
            return self.name_user        

