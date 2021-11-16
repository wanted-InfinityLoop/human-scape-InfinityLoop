import requests
import sys

from django.http import JsonResponse


class OpenAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.clinical_url = f"https://api.odcloud.kr/api/3074271/v1/uddi:cfc19dda-6f75-4c57-86a8-bb9c8b103887?page=1&perPage={sys.maxsize}"

    def get_clinical_trial(self):
        response = requests.get(self.clinical_url + "?serviceKey=" + self.api_key, timeout=3)

        if response.status_code == 401:
            return JsonResponse({"message": "UNAUTHORIZED_ERROR"})
        
        if response.status_code == 500:
            return JsonResponse({"message": "API_SERVER_ERROR"})

        return response.json()