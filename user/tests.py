from django.test import TestCase

# Create your tests here.

def test_contact(self):
    response = self.client.get(reverse('contact'))
    self.assertEqual(response.status_code, 200)

    self.assertContains(response, 'Reach out')


def test_Manager(self):


def test_superuser(self, email, username)



def test_User(AbstractBaseUser)

