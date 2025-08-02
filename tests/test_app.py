import unittest
from main import app, init_db

class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        init_db()
        self.client = app.test_client()

    def test_home_status(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_add_message(self):
        response = self.client.post('/add', data={'content': 'Test Message'}, follow_redirects=True)
        self.assertIn(b'Test Message', response.data)

if __name__ == '__main__':
    unittest.main()
