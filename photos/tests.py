from django.test import TestCase
from .models import Image, Category, Location

# Create your tests here.
class TestImage(TestCase):
    def setUp(self):
        self.location = Location(locationName='Nairobi')
        self.location.saveLocation()

        self.category = Category(categoryName='nature')
        self.category.saveCategory()

        self.testInstance = Image(id=1, imageName='IMG__001', imageDescription=' a test image', imageLocation=self.location,
                                imageCategory=self.category)

    def test_instance(self):
        self.assertTrue(isinstance(self.testInstance, Image))

    def test_save_image(self):
        self.testInstance.saveImage()
        filterImage= Image.objects.all()
        self.assertTrue(len(filterImage) > 0)

    def test_delete_image(self):
        self.testInstance.deleteImage()
        images = Image.objects.all()
        self.assertTrue(len(images) == 0)

    def test_update_image(self):
        self.testInstance.saveImage()
        self.testInstance.updateImage(self.testInstance.id, 'images/img.jpg')
        imgUpdt = Image.objects.filter(image='images/test.jpg')
        self.assertTrue(len(imgUpdt) > 0)

    def test_get_image_by_id(self):
        imageF = self.testInstance.getimageById(self.testInstance.id)
        image = Image.objects.filter(id=self.testInstance.id)
        self.assertTrue(imageF, image)

    def test_search_image_by_location(self):
        self.testInstance.saveImage()
        foundImages = self.testInstance.filterimageByLocation(imageLocation='Nairobi')
        self.assertTrue(len(found_images) == 1)

    def test_search_image_by_category(self):
        category = 'nature'
        foundImages = self.testInstance.searchImage(category)
        self.assertTrue(len(found_img) > 1)

    def tearDown(self):
        Image.objects.all().delete()
        Location.objects.all().delete()
        Category.objects.all().delete()

class TestLocation(TestCase):
    def setUp(self):
        self.location = Location(name='Nairobi')
        self.location.saveLocation()

    def test_instance(self):
        self.assertTrue(isinstance(self.location, Location))

    def test_save_location(self):
        self.location.saveLocation()
        locations = Location.getLocations()
        self.assertTrue(len(locations) > 0)

    def test_get_locations(self):
        self.location.saveLocation()
        locations = Location.getLocations()
        self.assertTrue(len(locations) > 1)

    def test_delete_location(self):
        self.location.deleteLocation()
        location = Location.objects.all()
        self.assertTrue(len(location) == 0)

class CategoryTestClass(TestCase):
    def setUp(self):
        self.category = Category(name='nature')
        self.category.saveCategory()

    def test_instance(self):
        self.assertTrue(isinstance(self.category, Category))

    def test_save_category(self):
        self.category.saveCategory()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)

    def test_delete_category(self):
        self.category.deleteCategory()
        category = Category.objects.all()
        self.assertTrue(len(category) == 0)
