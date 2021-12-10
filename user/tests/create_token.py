from test_plus import APITestCase
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


class CreateTokenTest(APITestCase):
    """JWT 토큰 생성 관련 테스트"""
    def setUp(self):
        User.objects.create(
            username='admin',
            email='bsb2121@naver.com',
            password=make_password('1234'),
        )

    def test1(self):
        user = User.objects.get(username='admin')
        self.assertNotEqual(user, None)

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
        access = response["access"]
        refresh = response["refresh"]

        self.assertNotEqual(access, None)
        self.assertNotEqual(refresh, None)

        # refresh a token
        self.post(
            '/auth/token/refresh/',
            data={
                'refresh': refresh,
            },
            extra={'format': 'json'},
        )
        self.response_200()
        response = self.last_response.json()
        print(response)
        access = response["access"]

        self.assertNotEqual(access, None)