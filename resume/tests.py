from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status

class PersonalDetailAPITest(APITestCase):
    
    def test_create_personal_detail(self):
        # Correct reverse URL lookup for the 'personal_detail-list'
        url = reverse('personal_detail-list')
        data = {
            "name": "John Doe",
            "email": "john@example.com",
            "phone": "1234567890",
            "github": "https://github.com/johndoe",
            "work_experience": [
                {
                    "company": "Tech Corp",
                    "start_month": "January",
                    "start_year": 2020,
                    "position": "Developer",
                    "location": "Remote"
                }
            ],
            "education": [
                {
                    "university": "XYZ University",
                    "start_year": 2015,
                    "end_year": 2019,
                    "degree": "B.Sc.",
                    "location": "City"
                }
            ],
            "skills": [
                {"skill_name": "Python"}
            ],
            "interests": [
                {"interest_name": "Reading"}
            ]
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
