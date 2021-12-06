from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_successful(self):
        """Test creating a new user is successful"""
        email = 'test@example.com'
        password = 'Password123'
        username = 'newuser123'
        user = get_user_model().objects.create_user(
            username=username,
			email=email,
			password=password
		)

        self.assertEqual(user.username, username)
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))


    def test_new_superuser(self):
        """Test creating a new superuser"""

        email = 'test@example.com'
        password = 'Password123'
        username = 'newsuperuser123'
        user = get_user_model().objects.create_superuser(
            username=username,
            email=email,
            password=password
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)