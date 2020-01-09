from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        '''Test creating a new user with an email is successful'''
        email = "mao@qiu.com"
        password = "test"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        '''Test the email of a new user is normalized'''
        email = "mao@QIUQIU.COM"
        user = get_user_model().objects.create_user(email, "test")
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        '''Test create user with invalid email raises error'''
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "test")

    def test_create_new_superuser(self):
        '''Test creating a new super user'''
        user = get_user_model().objects.create_superuser("mao@qiu.com", "test")
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
