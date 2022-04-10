
from django.test import TestCase
from .models import Profile, Post, Rating

# Set up method 
# Set up method 
class ProfileTestClass(TestCase):
    def setUp(self):
        self.profile=Profile(name='juliet')

    def test_instance(self):
        self.assertTrue(isinstance(self.profile, Profile))

#Testing Save Method

    

# Set up method        


class PostTestClass(TestCase):
    def setUp(self):
        self.post=Post(post='hey')

    def test_instance(self):
        self.assertTrue(isinstance(self.post, Post))  



# # Set up method        


class RatingTestClass(TestCase):
    def setUp(self):
        self.rating=Rating(user='project')

    def test_instance(self):
        self.assertTrue(isinstance(self.rating, Rating))  


        





        


