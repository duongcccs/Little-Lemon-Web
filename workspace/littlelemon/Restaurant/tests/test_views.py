from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
#from django.test import TestCase 
from django.test import TestCase  # Make sure TestCase is imported
from rest_framework.test import APIClient
from rest_framework import status
from Restaurant.models import Menu
from Restaurant.serializers import MenuSerializer


class MenuViewTest(TestCase):
    def setUp(self):
        # Set up some MenuItem instances for testing
        self.menu_item_1 = Menu.objects.create(title="Burger", price=120, inventory=50)
        self.menu_item_2 = Menu.objects.create(title="Pizza", price=250, inventory=30)
        self.menu_item_3 = Menu.objects.create(title="Pasta", price=180, inventory=40)

        # Create a user and get the auth token
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = Token.objects.create(user=self.user)

        # Create an APIClient instance to interact with the API
        self.client = APIClient()

        # Add the token to the request header
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_get_all_menu(self):
        # Make a GET request to the Menu API
        response = self.client.get('/restaurant/menu/')  # Adjust the URL if necessary
        
        # Get the expected serialized data
        menu = Menu.objects.all()
        serializer = MenuSerializer(menu, many=True)
        
        # Assert the response data is equal to the serialized data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
