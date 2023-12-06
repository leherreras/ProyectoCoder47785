from django.contrib.auth.models import User
from django.test import TestCase

from accounts.models import Avatar


class AvatarTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(
            username="pepe",
            password="pepe"
        )
        Avatar.objects.create(
            user=user,
            imagen="/media/avatares/Captura_de_pantalla_2023-12-04_194956.png"
        )

    def test_crecion_avatares(self):
        """Animals that can speak are correctly identified"""
        avatar = Avatar.objects.get(imagen="/media/avatares/Captura_de_pantalla_2023-12-04_194956.png")

        self.assertEqual(avatar.user.username, 'pepe')
