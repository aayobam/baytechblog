from django.test import TestCase, SimpleTestCase


# Create your tests here.
class AccountTestCase(SimpleTestCase):
    
    def test_register_status_code(self):
        response = self.client.get('/accounts/register/')
        self.assertEqual(response.status_code, 200)
        
        
    def test_login_status_code(self):
        response = self.client.get('/accounts/login/')
        self.assertEqual(response.status_code, 200)
      

    def test_logout_status_code(self):
        response = self.client.get('/accounts/log-out/')
        self.assertEqual(response.status_code, 200)
    

    
    def test_profile_status_code(self):
        response = self.client.get('/accounts/user/profile/')
        self.assertEqual(response.status_code, 200)
    
        
    def test_rest_password_status_code(self):
        response = self.client.get('/accounts/reset-password/')
        self.assertEqual(response.status_code, 200)
        
        
    def test_reset_password_sent_status_code(self):
        response = self.client.get('/accounts/reset-password-sent/')
        self.assertEqual(response.status_code, 200)
        
    
    def test_reset_status_code(self):
        response = self.client.get('/accounts/reset/<uidb64>/<token>/')
        self.assertEqual(response.status_code, 200)
        
        
    def test_reset_password_complete_status_code(self):
        response = self.client.get('/accounts/reset-password-complete/')
        self.assertEqual(response.status_code, 200)
        
    