import requests

class ACtivitySuggester:
    def suggest(self):
        response = self._make_request_to_api()
        return f"Why not: {response['activity']}"
    
    def _make_request_to_api(self):
        response = requests.get("http://www.boredapi.com/api/activity")
        return response.json


activity_suggester = ACtivitySuggester()

    