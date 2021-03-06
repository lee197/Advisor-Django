from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from core.models import SeekingTags

from profiles.serializers import SeekingTagSerializer

SEEKERINGTAGS_URL = reverse('profile:seekingtags-list')


class PrivateSeekingAPITests(TestCase):
    """Test mentortags can be retrieved by authorized user"""

    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            'test@londonappdev.com',
            'testpass'
        )
        self.client.force_authenticate(self.user)

    def test_retrieve_mentoringtags_list(self):
        """Test retrieving a list of mentortags"""
        SeekingTags.objects.create(user=self.user, name='kale')
        SeekingTags.objects.create(user=self.user, name='salt')

        res = self.client.get(SEEKERINGTAGS_URL)

        mentoringtags = SeekingTags.objects.all().order_by('-name')
        serializer = SeekingTagSerializer(mentoringtags, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data["results"], serializer.data)

    def test_create_mentoringtags_successful(self):
        """Test creating a new ingredient"""
        payload = {'name': 'Cabbage'}
        self.client.post(SEEKERINGTAGS_URL, payload)

        exists = SeekingTags.objects.filter(
            user=self.user,
            name=payload['name']
        ).exists()
        self.assertTrue(exists)

    def test_create_mentoringtags_invalid(self):
        """Test creating invalid mentortag fails"""
        payload = {'name': ''}
        res = self.client.post(SEEKERINGTAGS_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
