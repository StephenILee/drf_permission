from test_plus import APITestCase
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


class CreateTokenTest(APITestCase):
    """JWT 토큰 생성 관련 테스트"""
    def setUp(self):
        self.user = User.objects.create(
            username='admin',
            email='bsb2121@naver.com',
            password=make_password('1234'),
            is_active=True
        )

        self.user2 = User.objects.create(
            username='user',
            email='other@naver.com',
            password=make_password('1234'),
            is_active=True
        )

        # create a token
        self.post(
            '/auth/token/',
            data={
                'username': 'admin',
                'password': '1234',
            },
            extra={'format': 'json'},
        )
        self.response_200()
        response = self.last_response.json()
        print(response)
        self.access = response["access"]
        self.refresh = response["refresh"]

    def test1(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access)
        self.get(
            f'/user_fbv/{self.user2.id}'
        )
        self.response_200()
        response = self.last_response.json()
        print(response)

    def test2(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access + 'zzz')
        self.get(
            f'/user_fbv/{self.user2.id}'
        )
        self.response_401()

    def test3(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access)
        self.get(
            f'/user_fbv2/{self.user2.id}'
        )
        self.response_200()
        response = self.last_response.json()
        print(response)

    def test4(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access)
        self.get(
            f'/user/{self.user2.id}/'
        )
        self.response_200()
        response = self.last_response.json()
        print(response)