from django.db import models

class Plant(models.Model):
    binomial_name = models.CharField(max_length=200)
    indian_name = models.CharField(max_length=200)
    image_url = models.URLField(default="https://www.ikea.com/PIAimages/0614197_PE686822_S5.JPG")
    is_featured = models.BooleanField(default=False)

    # def get_all_objects(self):
    #     queryset = self._meta.model.objects.all()
    #     # can use the below method also
    #     # queryset = self.__class__.objects.all()   
    #     return queryset