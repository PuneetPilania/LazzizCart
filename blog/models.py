from django.db import models

class BlogPost(models.Model):
    post_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    title=models.CharField(max_length=50)
    head0=models.CharField(max_length=700,default="")
    chead0=models.CharField(max_length=7000,default="")
    head1=models.CharField(max_length=700,default="")
    chead1=models.CharField(max_length=7000,default="")
    head2=models.CharField(max_length=700,default="")
    chead2=models.CharField(max_length=7000,default="")
    pub_date=models.DateField()
    thumbnail=models.ImageField(upload_to="shop/images", default="")


    def __str__(self):
        return self.title
