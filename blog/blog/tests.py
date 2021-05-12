from django.test import SimpleTestCase


class BlogTest(SimpleTestCase):
    
    def test_post_list_status_code(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
        
    def test_post_detail_status_code(self):
        response = self.client.get('/<int:pk>/')
        self.assertEqual(response.status_code, 200)
        
        
    def test_new_post_status_code(self):
        response = self.client.get('/post/new/')
        self.assertEqual(response.status_code, 200)
        
        
    def test_edit_post_status_code(self):
        response = self.client.get('/post/<int:pk>/edit/')
        self.assertEqual(response.status_code, 200)
        
        
    def test_delete_post_status_code(self):
        response = self.client.get('/post/<int:pk>/delete/')
        self.assertEqual(response.status_code, 200)
        
        
    def test_edit_comment_status_code(self):
        response = self.client.get('/comment/<int:pk>/edit/')
        self.assertEqual(response.status_code, 200)
        
    
    def test_delete_comment_status_code(self):
        response = self.client.get('/comment/<int:pk>/delete/')
        self.assertEqual(response.status_code, 200)