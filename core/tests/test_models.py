from django.test import TestCase
from django.contrib.auth import get_user_model
from core import models


def sample_user(email='test@gmail.com', password='testpass'):
    """Create a sample user"""
    return get_user_model().objects.create_user(email, password)


class ModelTest(TestCase):

    def test_create_user_with_email_successful(self):
        """test creating a new user with an email is successful"""
        email = 'test@gamil.com'
        password = 'Testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """test normalised email with different cases"""
        email = 'test@GMAIL.com'
        user = get_user_model().objects.create_user(email, "test123")

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """test create user with no email raise error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "test123")

    def test_create_new_superuser(self):
        """Testing creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'test@gmail.com',
            'test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_mentor_tag_str(self):
        """Test the tag string representation"""
        mentor_tag = models.MentoringTags.objects.create(
            user=sample_user(),
            name='coding'
        )

        self.assertEqual(str(mentor_tag), mentor_tag.name)

    def test_seeker_tag_str(self):
        """Test the ingredient string representation"""
        seeker_tag = models.SeekingTags.objects.create(
            user=sample_user(),
            name='teaching'
        )

        self.assertEqual(str(seeker_tag), seeker_tag.name)
