from django.test import TestCase

# Create your tests here.
from django.contrib import auth

class AuthTestCase(TestCase):
    def setUp(self):
        self.u = User.objects.create_user('test@dom.com', 'test@dom.com', 'pass')
        self.u.is_staff = True
        self.u.is_superuser = True
        self.u.is_active = True
        self.u.save()

    def testLogin(self):
        self.client.login(username='test@dom.com', password='pass')

class AlreadyExistsFilenameUploaded(TestCase):
    def setUp(self):
        pass
    def test_resolve_duplicate_filename(self):
        #Добавить тестовое изображение трудовой книжки.
        pass

class AlreadyExistsFilenameResized(TestCase):
    def setUp(self):
        pass
    def test_resolve_duplicate_filename_of_resized_image(self):
        pass

class CheckOnlyUrlOrFilePathGivenInForm(TestCase):
    def setUp(self):
        #Create form, fill both fields, emulate POST request, show error.
        pass
    def test_display_error_on_both_fields_filled_in_upload_form(self):
        pass

class MiniLoadTest(TestCase):
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
    
    """
    def setUp(self):
        #check lenna.png/download if needed.
        from resizer import *

    def test_resizer_no_values_given(self): #should raise or succeed?
        dst = "lenna_200x200.png"
        res, msg = resize(src,dst)

    def test_resizer_both_values_and_wrong_ratio_given(self): #should raise.
        dst = "lenna_250x200.png"
        res, msg = resize(src,dst,w=250,h=200)

    def test_resizer_almost_but_not_perfect_ratio_given(self): #should raise.
        dst = "lenna_201x200.png"
        res, msg = resize(src,dst,w=201,h=200) # OK

    def test_resizer_correct_ratio_given(self): #should succeed.
        dst = "lenna_200x200.png"
        res, msg = resize(src,dst,w=200,h=200)

    def test_one_value_given(self):
        dst = "lenna_250x250.png"
        res, msg = resize(src,dst,w=250)
