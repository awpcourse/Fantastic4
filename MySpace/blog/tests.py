from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


class LoginViewTests(TestCase):

    def test_login_successful(self):
        User.objects.create_user(username='Daniela', password='1234')
        response = self.client.post(reverse('login'),
                                        {'username': 'Daniela',
                                        'password': '1234'})
        self.assertRedirects(response, '/blog/')

    def test_login_failure(self):
        User.objects.create_user(username='Daniela', password='1234')
        response = self.client.post(reverse('login'),
                                {'username': 'Daniela',
                                'password': 'fail'})
        self.assertContains(response, 'Wrong username or password')


class RegisterViewTests(TestCase):
    def test_register_Non_alphanumeric_username(self):
        invalid_data_dict = {
            'first_name': 'Daniela',
            'last_name': 'Birsan',
            'birth_date': '01/01/1993',
            'email': 'daniela@example.com',
            'username': 'da/na',
            'password1': 'secret',
            'password2': 'secret',
            }
        response = self.client.post(reverse('register'), invalid_data_dict)
        self.assertEquals(response.status_code, 200)

    def test_register_Already_existing_username(self):
        invalid_data_dict = {            
            'first_name': 'Daniela',
            'last_name': 'Birsan',
            'birth_date': '01/01/1993',
            'email': 'daniela@example.com',
            'username': 'daniela',
            'password1': 'secret',
            'password2': 'secret',
            }
        response = self.client.post(reverse('register'), invalid_data_dict)
        self.assertEquals(response.status_code, 200)

    def test_register_Mismatched_passwords(self):
        invalid_data_dict = {
            'first_name': 'Daniela',
            'last_name': 'Birsan',
            'birth_date': '01/01/1993',
            'email': 'daniela@example.com',
            'username': 'daniela',
            'password1': 'secret',
            'password2': 'fail',
            }
        response = self.client.post(reverse('register'), invalid_data_dict)
        self.assertEquals(response.status_code, 200)
