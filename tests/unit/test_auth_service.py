import unittest

from app.services.auth.auth_service import generate_token


class TestAuthService(unittest.TestCase):
    def test_generate_token(self):
        # Test generating token
        user_id = 1
        token = generate_token(user_id)
        self.assertTrue(isinstance(token, str))
        # Add more assertions as needed


if __name__ == '__main__':
    unittest.main()
