from django.db import models
from cloudinary.models import CloudinaryField

class Location(models.Model):
    name = models.CharField(max_length = 50)

    def __str__(self):
        return self.name 

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    @classmethod
    def update_location(cls,id,value):
        cls.objects.filter(id=id).update(name=value)

    @classmethod
    def display_all_locations(cls):
        return cls.objects.all()

class Category(models.Model):
    name = models.CharField(max_length = 30)

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()

    
    def delete_category(self):
        self.delete()

    @classmethod
    def update_category(cls,id,value):
        cls.objects.filter(id = id).update(name = value)    

class Image(models.Model):
    image= CloudinaryField()
    name = models.CharField(max_length = 30)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE ,default = "category")
    location = models.ForeignKey(Location, on_delete=models.CASCADE,default = "location")
    post_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()
    
    @classmethod
    def display_all_images(cls):
        return cls.objects.all()

    @classmethod
    def update_image_description(cls,id, value):
        cls.objects.filter(id=id).update(description = value)

    @classmethod
    def get_image_by_id(cls,id):
        return cls.objects.get(id=id)

    @classmethod
    def search_image(cls,category_search):
        try:
            searched_category = Category.objects.get(name= category_search)
            images = Image.objects.filter(category = searched_category.id)
            return images
        except Exception:
            return "No images were found for that category"

    @classmethod
    def filter_by_location(cls, location_search):
    
        searched_location = Location.objects.get(name = location_search)
        images = Image.objects.filter(location = searched_location.id)
        return images 
        