from django.test import TestCase
from unittest.suite import TestSuite
from .models import Profile,Post,Image,Self
from django.contrib.auth.models import User

# Create your tests here.
class ProfileTest(TestCase):
    def setUp(self):
        self.tess = User(username = 'nimo',email = 'nimotriz@gmail.com')
        self.tess = Profile(user = Self.nimo,user = 1,bio = 'tests',profilePhoto = 'test.jpg', contacts='0700220022')

    def test_instance(self):
        self.assertTrue(isinstance(self.tess,Profile))

    def test_save_profile(self):
        Profile.save_profile(self)
        all_profiles = Profile.objects.all()
        self.assertTrue(len(all_profiles),0)

    def test_delete_profile(self):
        self.tess.delete_profile()
        all_profiles = Profile.objects.all()
        self.assertEqual(len(all_profiles),0)



class PostTestCase(TestCase):
    def setUp(self):
        self.new_post = Post(title = 'delani',image = 'test.jpg',description = 'testD',url = 'https://test.com',user = TestSuite)


    def test_save_post(self):
        self.new_post.save_project()
        images = Image.objects.all()
        self.assertEqual(len(images),1)

    def test_delete_post(self):
        self.new_post.delete_post()
        images = Post.objects.all()
        self.assertEqual(len(images),1)
