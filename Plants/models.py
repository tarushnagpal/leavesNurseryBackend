from django.db import models

class Categories(models.Model):
    
    category_name = models.CharField(max_length=100)
    category_id = models.AutoField(primary_key=True)

    def __str__(self):
        return "%s" % (self.category_name)

class Plant(models.Model):

    category = models.ForeignKey(Categories, on_delete=models.CASCADE, default="New Category")

    binomial_name = models.CharField(max_length=200)
    indian_name = models.CharField(max_length=200)
    image_url = models.URLField(default="https://www.ikea.com/PIAimages/0614197_PE686822_S5.JPG")
    is_featured = models.BooleanField(default=False)

    # def get_all_objects(self):
    #     queryset = self._meta.model.objects.all()
    #     # can use the below method also
    #     # queryset = self.__class__.objects.all()   
    #     return queryset