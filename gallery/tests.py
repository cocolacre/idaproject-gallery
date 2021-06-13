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
        pass #

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
    def test_validate_minimal_load_endurance(self):
        #Validate minimal load threshold (1 request per second?)
    def test_failsafe(self):    
        #Expectedly fail OR display "service-overloaded-try-again-later" message to user.
        
        