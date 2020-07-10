from django.db import models

# Create your models here.
<<<<<<< HEAD
class Category(models.Model):
    category_name = models.CharField(max_length=100)
    
class Post(models.Model):
    category = models.IntegerField()
    post_text = models.CharField(max_length=1000)
    post_title = models.CharField(max_length=100)
    post_price = models.IntegerField()
    post_contact = models.CharField(max_length=100,default='')
    post_owner = models.CharField(max_length=100,default='')
    pub_date = models.DateTimeField('date published')
=======
>>>>>>> c83d230948e5225f752cf55d34ff15e2b2765ece
