from django.contrib import admin
from .models import Order

# Register your models here.


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display=['id','flavour','order_status','size']
    list_filter=['created_at','updated_at','order_status']