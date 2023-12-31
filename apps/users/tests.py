from django.contrib.auth import get_user
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class RegisterTestCase(TestCase):

    def test_user_is_create(self):
        self.client.post(
            reverse('users:register'), data={
                "first_name": "Shohjahon",
                "last_name": "Shohjahon",
                "username": "Shohjahon",
                "email": "Shohjahon@gmail.com",
                "password": "Shohjahon"
            }
        )

        user = User.objects.get(username="Shohjahon")
        #
        self.assertEqual(user.first_name, "Shohjahon")
        self.assertEqual(user.last_name, "Shohjahon")
        self.assertEqual(user.username, 'Shohjahon')
        self.assertEqual(user.email, 'Shohjahon@gmail.com')
        # self.assertEqual(user.password, 'Shohjahon')
        self.assertTrue(user.check_password("Shohjahon"))

    def test_required_fields(self):
        response = self.client.post(
            reverse('users:register'), data={
                "first_name": "Shohjahon",
            }
        )
        user_count = User.objects.count()

        self.assertEqual(user_count, 0)

        self.assertFormError(response,"form", "username", "This field is required.")
        self.assertFormError(response, "form", "email", "This field is required.")
        self.assertFormError(response, "form", "password", "This field is required.")

    def test_invalide_email(self):
        response = self.client.post(
            reverse('users:register'),
            data={
                "first_name": "Shohjahon",
                "last_name": "Shohjahon",
                "username": "Shohjahon",
                "email": "Shohjahongmail.com",
                "password": "Shohjahon"
            }
        )
        user_count = User.objects.count()

        self.assertEqual(user_count, 0)

        self.assertFormError(response, 'form', 'email', "Enter a valid email address.")

    def test_unique_fields(self):
        User.objects.create(email='Shohjahon@gmail.com', username='Shohjahon')

        resp = self.client.post(
            reverse('users:register'),
            data={
                "first_name": "Shohjahon",
                "last_name": "Shohjahon",
                "username": "Shohjahon",
                "email": "Shohjahon@gmail.com",
                "password": "Shohjahon"
            }
        )

        user_count = User.objects.count()

        self.assertEqual(user_count, 1)
        self.assertFormError(resp, 'form', 'email', 'email already exists')

        resp = self.client.post(
            reverse('users:register'),
            data={
                "first_name": "Shohjahon",
                "last_name": "Shohjahon",
                "username": "Shohjahon",
                "email": "Shohjahon@gmail.com",
                "password": "Shohjahon"
            }
        )
        self.assertEqual(user_count, 1)
        self.assertFormError(resp, 'form', 'username', 'A user with that username already exists.')
class LoginTestCase(TestCase):
    def setUp(self):
        self.db_user = User.objects.create(first_name='first_name', last_name='last',  username='shohjahon1', email='shohjahon1@gmail.com')
        self.db_user.set_password('nimadir')
        self.db_user.save()

    def test_is_login(self):
        self.client.post(
            reverse("users:login"),
            data={
                "username": "shohjahon1",
                "password": "nimadir"
            }
        )
        user = get_user(self.client)

        self.assertTrue(user.is_authenticated)


class ProfileTestCase(TestCase):
    def setUp(self):
        self.db_user = User.objects.create(first_name='first_name', last_name='last', username='shohjahon1', email='shohjahon1@gmail.com')
        self.db_user.set_password('nimadir')
        self.db_user.save()

    def test_login_reuqired(self):
        response = self.client.get(reverse('users:profile'))
        self.assertEqual(response.url, reverse('users:login') + '?next=/users/profile/')

    def test_profile_details(self):
        self.client.login(username='shohjahon1', password='nimadir')

        response = self.client.get(reverse('users:profile'))

        self.assertContains(response, self.db_user.first_name)
        self.assertContains(response, self.db_user.last_name)
        self.assertContains(response, self.db_user.username)
        self.assertContains(response, self.db_user.email)

    def test_logout(self):
        self.client.login(username='shohjahon1', password='nimadir')

        self.client.get(reverse('users:logout'))
        user = get_user(self.client)

        self.assertFalse(user.is_authenticated)
