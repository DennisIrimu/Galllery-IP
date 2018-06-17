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
