from django.db import models
from django.utils.safestring import mark_safe
# Create your models here.
STA = (
    ("0","Inactive"),
    ("1","Active")
)
GEN = (
    ("0","MALE"),
    ("1","FEMALE"),
    ("2","OTHER"),
)
P_STA = (
    ('AVL', 'Available'),
    ('NA', 'Not Available'),
)
C_STA = (
    ("0","PENDING"),
    ("1","CONFIRM"),
    ("2","CANCEL")
)
PMODE = (
    ("0","OFFLINE"),
    ("1","ONLINE")
)
PAY_STA = (
    ("0","PENDING"),
    ("1","CONFIRM"),
    ("2","CANCEL")
)

class Login(models.Model):
    Email = models.EmailField()
    Name = models.CharField(max_length=25,null=True)
    Phone_no = models.BigIntegerField()
    Password = models.CharField(max_length=20,null=True)
    Conf_Password = models.CharField(max_length=20,null=True)
    Reg_Date = models.DateTimeField(auto_now_add=True)
    Role = models.CharField(max_length=30)
    Status = models.CharField(max_length=30)

    def __str__(self):
        return self.Name

class User_Details(models.Model):
    Login_id = models.ForeignKey(Login,on_delete=models.CASCADE)
    DOB = models.DateField()
    Photo = models.ImageField(upload_to='photos')
    Gender = models.CharField(max_length=10,choices=GEN)
    Address = models.TextField()
    City_name = models.CharField(max_length=30)

    def user_photo(self):
        return mark_safe('<img src="{}" width="100"/>'.format(self.Photo.url))

    user_photo.allow_tags = True

class Category(models.Model):
    Cat_name = models.CharField(max_length=25)

    def __str__(self):
        return self.Cat_name

class Product(models.Model):
    Login_id = models.ForeignKey(Login, on_delete=models.CASCADE)
    Cat_id = models.ForeignKey(Category,on_delete=models.CASCADE)
    Product_name = models.CharField(max_length=25)
    Product_image = models.ImageField(upload_to='photos',null=True)
    Product_description = models.TextField()
    Quantity = models.CharField(null=True,max_length=30)
    unit = models.CharField(max_length=10,null=True)
    Product_price = models.FloatField()
    Old_Product_price = models.FloatField(null=True)
    Product_Status = models.CharField(max_length=3,choices=P_STA)


    def __str__(self):
        return self.Product_name
    def Product_images(self):
        return mark_safe('<img src="{}" width="100"/>'.format(self.Product_image.url))

    Product_images.allow_tags = True


class Order(models.Model):
    Login_id = models.ForeignKey(Login, on_delete=models.CASCADE,null=True)
    finaltotal = models.IntegerField(null=True)
    name = models.CharField(max_length=40,null=True)
    address = models.TextField(null=True)
    Payment_mode = models.CharField(max_length=25,null=True)
    Pay_Status = models.CharField(max_length=3,null=True)
    timestamp = models.DateTimeField(auto_now_add=True,null=True)
    status = (
        ('placed','placed'),
        ('cancel','cancel')
    )
    STATUS = models.CharField(max_length=20,choices=status,default="placed")


class Feedback(models.Model):
    Login_id = models.ForeignKey(Login, on_delete=models.CASCADE,null=True)
    Rating = models.IntegerField(null=True)
    Comment = models.TextField(null=True)
    Date = models.DateTimeField(auto_now_add=True)

class Complain(models.Model):
    Login_id = models.ForeignKey(Login, on_delete=models.CASCADE,null=True)
    Subject = models.CharField(max_length=50,null=True)
    Message = models.TextField(null=True)

class Contact_us(models.Model):
    Name = models.CharField(max_length=30,null=True)
    Subject = models.CharField(max_length=30, null=True)
    Email_id = models.EmailField()
    Phone_no = models.BigIntegerField()
    Message = models.TextField()
    Timestamp = models.DateTimeField(auto_now_add=True)

class Cart(models.Model):
    userid = models.ForeignKey(Login, on_delete=models.CASCADE,null=True)
    productid = models.ForeignKey(Product, on_delete=models.CASCADE,null=True)
    quantity = models.IntegerField(null=True)
    totalamount = models.IntegerField(null=True)
    cartstatus = models.IntegerField(null=True)
    orderid = models.IntegerField(null=True)



class cardDetail(models.Model):
    nameoncard = models.CharField(max_length=40)
    card_number = models.CharField(max_length=16)
    card_cvv = models.CharField(max_length=3)
    exp_date = models.CharField(max_length=10)
    card_balance = models.FloatField()



# class Store(models.Model):
#     Store_title = models.CharField(max_length=100)
#     Store_image = models.ImageField(upload_to='photos')
#     Store_desc = models.TextField()
#     address = models.CharField(max_length=100)
#     contact = models.CharField(max_length=10)
#     user = models.ForeignKey(Login,on_delete=models.CASCADE)
#     date = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return self.Store_title
#     def Store_images(self):
#         return mark_safe('<img src="{}" width="100"/>'.format(self.Store_image.url))
#
#     Store_images.allow_tags = True