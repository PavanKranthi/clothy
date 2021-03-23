from django.db import models

# Create your models here.
class Category(models.Model):
    category_code = models.CharField(max_length=50)
    cateogry_sub_code = models.CharField(max_length=20)

class Product(models.Model):
    category_code = models.ForeignKey('Category',on_delete = models.CASCADE)
    cateogry_sub_code = models.ForeignKey('Category')
    product_code = models.CharField(max_length=30)
    product_sub_code = models.CharField(max_length=30)
    product_name = models.CharField(max_length=100)
    product_dscrptn = models.CharField(max_length=1000)
    product_color = models.CharField(max_length=10)
    fabric_name = models.CharField(max_length=30)
    net_components = models.CharField(max_length=30)
    product_cost = models.DecimalField(max_digits=20,decimal_places=4)
    product_ccy = models.CharField(max_length=3)
    prod_discount = models.DecimalField(max_digits=20,decimal_places=4)
    prod_sell_price = models.DecimalField(max_digits=20,decimal_places=4)
    prod_sell_price_ccy = models.CharField(max_length=3)
    prod_size = models.CharField(max_length=5)
    promo_remarks = models.CharField(max_length=2500)
    product_remarks = models.CharField(max_length=2500)
    manufacturer_code = models.CharField(max_length=5)
    additional_info_1 = models.CharField(max_length=2500)
    additional_info_2 = models.CharField(max_length=2500)
    additional_info_3 = models.CharField(max_length=2500)
    additional_info_4 = models.CharField(max_length=2500)
    additional_info_5 = models.CharField(max_length=2500)
    country_origin = models.CharField(max_length=5)
    prod_image = models.CharField(max_length=2500)
    prod_weight = models.DecimalField(max_digits=20,decimal_places=4)
    created_dt = models.DateTimeField(auto_now=False,auto_now_add=True)
    created_by = models.CharField(max_length=500)
    last_upd_dt = models.DateTimeField(auto_now=True,auto_now_add=True)
    last_upd_by = models.CharField(max_length=500)
    free_text_1v = models.CharField(max_length=5000)
    free_text_2d = models.DateField()
    free_text_3n = models.DecimalField()
    free_text_4t = models.DateTimeField()
    prod_wear_type = models.CharField(max_length=100)
    age_range_code = models.CharField()
    cupon_id_list = models.CharField()
    material_care = models.CharField(max_length=100)
    points_applicable = models.IntegerField()
    points_expriy_date = models.DateField()

class ProductReview(models.Model):
    product_sub_code = models.ForeignKey('Product',on_delete=models.CASCADE)
    ratings = models.DecimalField()
    comments = models.CharField(max_length=2000)
    customer_id = models.ForeignKey('CUSTOMER',on_delete=models.CASCADE)

class ProductImages(models.Model):
    product_sub_code = models.ForeignKey('Product',on_delete=models.CASCADE)
    image_id = models.CharField(max_length=50)
    image_file_path = models.CharField(max_length=2500)

class ProductDiscount(models.Model):
    product_sub_code = models.ForeignKey('Product',on_delete=models.CASCADE)
    discount_code = models.CharField(max_length=30)
    prod_discount = models.DecimalField(max_digits=20,decimal_places=4)
    max_discount = models.DecimalField(max_digits=20,decimal_places=4)
    prod_discount_value = models.DecimalField(max_digits=20,decimal_places=4)
    max_discount_value = models.DecimalField(max_digits=20,decimal_places=4)

class ProductInventory(models.Model):
    product_sub_code = models.ForeignKey('Product',on_delete=models.CASCADE)
    quantity_available = models.IntegerField()
    quantity_sold = models.IntegerField()





