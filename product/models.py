from django.db import models

# Create your models here.

class CdtCategory(models.Model):
    tx_category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.tx_category_name


class CdtSubcategory(models.Model):
    tx_subcategory_name = models.CharField(max_length=50)
    id_category = models.ForeignKey(CdtCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.tx_subcategory_name


class CdtBrand(models.Model):
    tx_brand_name = models.CharField(max_length=50)

    def __str__(self):
        return self.tx_brand_name

class CdtVendor(models.Model):
    tx_name_vendor = models.CharField(max_length=50)
    nm_phone_number_vendor = models.CharField(max_length=10)
    tx_description = models.CharField(max_length=50)

    def __str__(self):
        return self.tx_name_vendor




class CdtProductPhoto(models.Model):
    tx_url_photo = models.ImageField(null=True, blank=True)
    bl_primary = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)
    
    """ @property
    def imageURL(self):
        url = self.tx_url_photo.url """

class TdtColor(models.Model):
    tx_name_color = models.CharField(max_length=75)
    id_photo = models.ForeignKey(CdtProductPhoto, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.tx_name_color
    

class CdtSize(models.Model):
    tx_name_size =  models.CharField(max_length=4)
    id_product_color = models.ManyToManyField(TdtColor)

    def __str__(self):
        return self.tx_name_size

class TdtProduct(models.Model):
    GENDER_CHOICES = [
        ('0', 'male'),
        ('1', 'female'),
        ('2', 'others')

    ]

    tx_product_name = models.CharField(max_length=75)
    tx_description = models.CharField(max_length=75)
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES)
    price_sale_unit = models.DecimalField(max_digits=8, decimal_places=2)
    id_subcategory = models.ForeignKey(CdtSubcategory, on_delete=models.CASCADE)
    id_brand = models.ForeignKey(CdtBrand, on_delete=models.CASCADE)
    id_vendor = models.ForeignKey(CdtVendor, on_delete=models.CASCADE)
    id_color = models.ManyToManyField(TdtColor)

    def __str__(self):
        return self.tx_product_name




