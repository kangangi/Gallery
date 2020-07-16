from django.test import TestCase
from .models import Location, Category, Image
from unittest import skip

class LocationTestClass(TestCase):
    '''
    Class that tests the location
    '''
    def setUp(self):
        '''
        Creates new instances before a test
        '''
        self.nairobi = Location(name = "nairobi")
        self.nairobi.save_location()
    
    def tearDown(self):
        '''
        Clears database after each test
        '''
        Location.objects.all().delete()

    def test_location_instance(self):
        '''
        This will test whether the new location created is an instance of the Location class
        '''
        self.assertTrue(isinstance(self.nairobi, Location))

    def test_save_location_method(self):
        '''
        This tests whether new loaction is added to the db 
        '''
        self.nairobi.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations)> 0)

    def test_delete_location(self):
        '''
        This tests whether location is deleted
        '''
        self.nairobi.save_location()
        locations1= Location.objects.all()
        self.assertEqual(len(locations1),1)
        self.nairobi.delete_location()
        locations2= Location.objects.all()
        self.assertEqual(len(locations2),0)

    def test_update_location(self):
        '''
        Tests whether the location name is updated
        '''
        self.nairobi.save_location()
        self.nairobi.update_location(self.nairobi.id,'naivasha')
        new_update = Location.objects.get(name = "naivasha")
        self.assertEqual(new_update.name, 'naivasha')

    def test_display_locations(self):
        '''
        This tests whether the display location function is getting the locations from the db
        '''
        self.nairobi.save_location()
        self.assertEqual(len(Location.display_all_locations()), 1)
    



class CategoryTestClass(TestCase):
    '''
    Class that tests the category
    '''
    def setUp(self):
        '''
        Creates new instances before a test
        '''
        self.nature = Category(name = "nature")
        self.nature.save_category()
    
    def tearDown(self):
        '''
        Clears database after each test
        '''
        Category.objects.all().delete()

    def test_category_instance(self):
        '''
        This will test whether the new location created is an instance of the Location class
        '''
        self.assertTrue(isinstance(self.nature, Category))

    def test_save_category_method(self):
        '''
        This tests whether new loaction is added to the db 
        '''
        self.nature.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories)> 0)

    def test_delete_category(self):
        '''
        This tests whether category is deleted
        '''
        self.nature.save_category()
        categories1 = Category.objects.all()
        self.assertEqual(len(categories1),1)
        self.nature.delete_category()
        categories2 = Category.objects.all()
        self.assertEqual(len(categories2),0)

    
    def test_update_category(self):
        '''
        Tests whether the category name is updated
        '''
        self.nature.save_category()
        self.nature.update_category(self.nature.id,'natural')
        new_update = Category.objects.get(name = "natural")
        self.assertEqual(new_update.name, 'natural')




class ImageTestClass(TestCase):
    '''
    Class that tests the images
    '''

    def setUp(self):
        '''
        Creates new instances before a test
        '''
        self.nature = Category( name= "nature")
        self.nairobi = Location(name = "nairobi")
        self.flower = Image(image = "image", name ='flower', description = 'beautiful', category= self.nature, location= self.nairobi)

        self.nature.save_category()
        self.nairobi.save_location()
        self.flower.save_image()

    def tearDown(self):
        '''
        Clears database after each test
        '''
        Image.objects.all().delete()
        Category.objects.all().delete()
        Location.objects.all().delete()

    def test_image_instance(self):
        '''
        This will test whether the new image created is an instance of the Image class
        '''
        self.assertTrue(isinstance(self.flower, Image))


    def test_save_image_method(self):
        '''
        This tests whether new image is added to the db 
        '''
        self.flower.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images)> 0)

    def test_display_images(self):
        '''
        This tests whether the display image function is getting the images from the db
        '''
        self.flower.save_image()
        self.assertEqual(len(Image.display_all_images()), 1)

    def test_delete_images(self):
        '''
        This tests whether image is deleted
        '''
        self.flower.save_image()
        images1 = Image.objects.all()
        self.assertEqual(len(images1),1)
        self.flower.delete_image()
        images2 = Image.objects.all()
        self.assertEqual(len(images2),0)

    def test_update_image_description(self):
        '''
        Tests whether the image description is updated
        '''
        self.flower.save_image()
        self.flower.update_image_description(self.flower.id,'pink')
        new_update = Image.objects.get(name = "flower")
        self.assertEqual(new_update.description, 'pink')


    def test_get_image_by_id(self):
        '''
        Tests whether image is retrieved by id 
        '''
        self.flower.save_image()
        image = Image.get_image_by_id(self.flower.id)
        self.assertEqual(image.name, self.flower.name)

    def test_search_image(self):
        '''
        Tests whether image is retrieved by category
        '''
        self.nature.save_category()
        self.flower.save_image()
        images = Image.search_image("nature")
        self.assertTrue(len(images) > 0)

    
    def test_search_location(self):
        '''
        Tests whether image is retrieved by location
        '''
        self.nairobi.save_location()
        self.flower.save_image()
        images = Image.filter_by_location("nairobi")
        self.assertTrue(len(images) > 0)

