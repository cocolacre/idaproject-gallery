import os
from .resizer import *
from django.test import TestCase
from django.contrib import auth
from django.contrib.auth.models import User

class AuthTestCase(TestCase):
    def setUp(self):
        self.u = User.objects.create_user('test@dom.com', 'test@dom.com', 'pass')
        self.u.is_staff = True
        self.u.is_superuser = True
        self.u.is_active = True
        self.u.save()

    def testLogin(self):
        self.client.login(username='test@dom.com', password='pass')

# Create your tests here.
class AlreadyExistsFilenameUploaded(TestCase):
    """
    Use selenium?
    Upload same file twice.
    """
    def setUp(self):
        pass
    def test_resolve_duplicate_filename(self):
        #Добавить тестовое изображение трудовой книжки.
        pass

class AlreadyExistsFilenameResized(TestCase):
    """
    
    """
    def setUp(self):
        pass
    def test_resolve_duplicate_filename_of_resized_image(self):
        pass

class BothUrlAndFilePathGivenInForm(TestCase):
    """
    Fill both fields (file path and URL) in upload_image form,
    raise error, notify user?
    """

    def setUp(self):
        #Create form, fill both fields, emulate POST request, show error.
        pass
    def test_display_error_on_both_fields_filled_in_upload_form(self):
        pass

class MiniLoadTest(TestCase):
    """
    Just kidding.
    """
    def setUp(self):
        #Use generators\coroutines to prepare N POST requests in M seconds to yield from.
        pass
    def test_validate_minimal_load_endurance(self):
        #Validate minimal load threshold (1 request per second?)
        pass
    def test_failsafe(self):    
        #Expectedly fail OR display "service-overloaded-try-again-later" message to user.
        pass

class TestResizer(TestCase):
    """
    We hate HARDCODED values. Do you?
        '...2.5.6 Removing hardcoded URLs in templates ...'
        '...The problem with this hardcoded, tightly-coupled approach is that it becomes challenging to change URLs on projects
        with a lot of templates....'
        '...we'll use 'reverse()' rather than a hardcoded URL...'
    """
    def setUp(self):
        #check lenna.png/download if needed.
        self.src = "lenna.png"
        self.resized_filenames = ["gallery/assets/lenna_200x200.png",
                                  "gallery/assets/lenna_201x200.png",
                                  "gallery/assets/lenna_204x200.png",
                                  "gallery/assets/lenna_250x250.png"]
        #NOTE: This is VERY BAD. Hope you don't notice. Just kidding.
        #TODO: remove hardcoded duplicate names.
    
    def tearDown(self): #NOTE: Very dirty. Gotta go fast.
        for f in self.resized_filenames:
            try:
                os.remove(f) #clean up test resized files.
            except Exception as _e:
                pass

    def test_resizer_no_values_given(self): #should raise silently.
        dst = "gallery/assets/lenna_200x200.png"
        res, msg = resize(self.src,dst)
        self.assertFalse(res)
        
    def test_resizer_both_values_and_wrong_ratio_given(self): #should raise silently.
        dst = "gallery/assets/lenna_250x200.png"
        res, msg = resize(self.src,dst,w=250,h=200)
        self.assertFalse(res)
        
    def test_resizer_almost_but_not_perfect_ratio_given(self): #should succeed.
        dst = "gallery/assets/lenna_201x200.png"
        res, msg = resize(self.src,dst,w=201,h=200) # OK
        self.assertTrue(res)
        
    def test_resizer_correct_ratio_given(self): #should succeed.
        dst = "gallery/assets/lenna_200x200.png"
        res, msg = resize(self.src,dst,w=200,h=200)
        self.assertTrue(res)
        
    def test_one_value_given(self): #should succeed. #these comments are wrong.
        dst = "gallery/assets/lenna_250x250.png"
        res, msg = resize(self.src,dst,w=250)
        self.assertTrue(res)
