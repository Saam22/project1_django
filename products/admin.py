from django.contrib import admin

# Register your models here.
from .models import Product , Female , Male , User, Order_Product, Video, User_Video

admin.site.register(Product),
admin.site.register(Female),
admin.site.register(Male),
admin.site.register(User),
admin.site.register(Order_Product),
admin.site.register(Video),
admin.site.register(User_Video)