import os
import requests
import google.generativeai as genai
from app.models.user import User
from app.services.diet_tracking import DietTrackingService

genai.configure(api_key=os.environ['GEMINI_API_KEY'])

class RecommendationService:
    @staticmethod
    def get_diet_advice(user_id, prompt_type):
        user = User.query.get(user_id)
        if not user:
            raise ValueError("User not found")

        # Fetch user's veggie data
        weekly_veggies = DietTrackingService.get_weekly_veggies(user_id)
        veggies_list = ', '.join(weekly_veggies)

        # Determine the prompt based on the type
        if prompt_type == 'quick_tip':
            prompt = f"Suggest a quick and easy additional vegetable or fruit to increase my weekly intake."
        elif prompt_type == 'recipe_tip':
            prompt = f"Suggest a recipe to increase and diversify my weekly vegetables or fruits intake."
        elif prompt_type == 'group_analysis':
            prompt = f"Analyze my vegetable and fruit intake and tell me which groups I am missing."

        # Full prompt with veggie list
        full_prompt = f"{prompt} Currently, I have consumed: {veggies_list}."

        # Proxy configuration
        proxies = {
            "http": os.getenv('PROXY_URL'),
            "https": os.getenv('PROXY_URL'),
        }

        # URL for the Gemini API
        api_key = os.getenv('GEMINI_API_KEY')
        url = f'https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}'

        # Headers
        headers = {
            'Content-Type': 'application/json'
        }

        # Data payload
        data = {
            "contents": [{
                "parts": [{
                    "text": full_prompt
                }]
            }]
        }

        # Making the POST request through the proxy
        response = requests.post(url, headers=headers, json=data, proxies=proxies)
        
        if response.status_code != 200:
            raise ValueError(f"Failed to fetch diet advice: {response.status_code}, {response.text}")

        # Extracting the text from the response
        response_json = response.json()
        if 'candidates' in response_json and len(response_json['candidates']) > 0:
            advice_text = response_json['candidates'][0]['content']['parts'][0]['text']
        else:
            advice_text = 'No advice available'

        return advice_text