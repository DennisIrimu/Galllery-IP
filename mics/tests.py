from django.test import TestCase
from .models import Location,Image,Category

# Create your tests here.
class LocationTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.new_location= Location(location = 'Nairobi')
        self.location.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.location, Location))

    def test_save_location(self):
        self.location.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)

    def test_update_location(self):
        self.new_location.save_location()
        location_id = self.new_location.id
        Location.update_location(id, "mombasa")
        self.assertEqual(self.new_location.location, "mombasa")

    def test_delete_location(self):
        self.location.delete_location()
        location = Location.objects.all()
        self.assertTrue(len(location) == 0)

    def tearDown(self):
        Location.objects.all().delete()

class CategoryTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.new_category= Category(category = 'travel')
        self.location.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.category, Category))


    def update_category(self):
        self.new_category.save_category()
        category_id = self.new_category.id
        Category.update_category(id,"travel")
        self.assertEqual(self.category.category,"travel")

    def test_delete_category(self):
        self.category.delete_category()
        category = Category.objects.all()
        self.assertTrue(len(category) == 0)

    def tearDown(self):
        Category.objects.all().delete()

class ImageTestClass(TestCase):
    #location
    def setUp(self):
        self.new_location= Location(location = 'Nairobi')
        self.location.save()
    #category
    def setUp(self):
        self.new_category= Category(category = 'travel')
        self.category.save()
    # Set up method
    def setUp(self):
        self.new_image= Image(image = 'image1.jpg',image_url = 'http://wallpaperstone.blogspot.com/2007/09/view-wallpaper-in-room.html',image_name = 'purple',image_description = 'purple table',image_location = 'Nairobi',image_category = 'travel')
        self.image.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.image, Image))

    def tearDown(self):
        Image.objects.all().delete()
        Location.objects.all().delete()
        Category.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.image,Image))

    def test_save_image(self):
        self.test_image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

    def update_image(self):
        self.new_category.save_category()
        category_id = self.new_category.id
        Category.update_category(id,"image1.jpg","purple table")
        self.assertEqual(self.category.category,"image1.jpg","purple table")

    def test_get_photo_by_id(self):
        search_image = self.image.get_photo_by_id(self.image.id)
        searched_image = Image.objects.filter(id=self.image.id)
        self.assertTrue(searched_image,search_image)

    def test_search_by_category(self):
        category = 1
        searched_image = self.image.search_by_category(category)
        self.assertTrue(len(searched_image) > 0)

    def test_filter_by_location(self):
        location = 1
        searched_image = self.image.filter_by_location(location)
        self.assertTrue(len(searched_image) > 1)

    def test_delete_image(self):
        self.image.save_image()
        self.image.delete_image()
        images = Image.objects.all()
        self.assertTrue(len(images) == 0)
