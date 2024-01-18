from django.test import TestCase
from django.urls import reverse
from .models import CustomUser
import json
import jwt



class RegistrationTestCase(TestCase):
    def setUp(self):
        # Any setup code needed before each test goes here
        pass

    def test_successful_registration(self):
        # Test successful user registration
        data = {'email': 'anu@gmail.com', 'password': 'test@123','first_name':'Anu','last_name':'K.S'}
        response = self.client.post(reverse('book:register'), data)
        self.assertEqual(response.status_code, 201)
        self.assertTrue(CustomUser.objects.filter(email='anu@gmail.com').exists())

    def test_duplicate_username(self):
        # Test registration with a duplicate username
        CustomUser.objects.create_user(email='athul@gmail.com', password='newpassword@123',first_name='Anu',last_name='Mohan')
        data = {'email': 'athul@gmail.com', 'password': 'newpassword','first_name':'Anu','last_name':'K.S'}
        response = self.client.post(reverse('book:register'), data)
        self.assertEqual(response.status_code, 400)
        self.assertIn('email', response.json())



class LoginTestCases(TestCase):
    def setUp(self):
        self.existing_user = CustomUser.objects.create_user(email='amjith@gmail.com', password='newpassword@123',first_name='Anu',last_name='Mohan')

    def test_successful_login(self):
        data={'email':'amjith@gmail.com','password':'newpassword@123'}
        response = self.client.post(reverse('book:login'),data)
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.json().get('message'), 'Login successful')
        self.assertIn('access', response.json())
        self.assertIn('refresh', response.json())
        access_token = response.json().get('access')
        refresh_token = response.json().get('refresh')
        access_payload = jwt.decode(access_token, verify=False)  # Set verify to True in production
        refresh_payload = jwt.decode(refresh_token, verify=False)

    def test_failure_login(self):
        # Test failed login with incorrect password
        data = {'email': 'amjith@gmail.com', 'password': 'wrongpassword@123'}
        response = self.client.post(reverse('book:login'), data)
        self.assertEqual(response.status_code, 400)
        # Test failed login with incorrect email
        data = {'email': 'amj@gmail.com', 'password': 'newpassword@123'}
        response = self.client.post(reverse('book:login'), data)
        self.assertEqual(response.status_code, 400)

        # Test failed login with missing credentials
        response = self.client.post(reverse('book:login'), {})
        self.assertEqual(response.status_code, 400)





