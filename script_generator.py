import requests

class ScriptGenerator:
    def __init__(self, api_key):
        self.api_key = api_key
        self.api_url = "https://gemini.api.endpoint/generate"  # Replace with actual Gemini API endpoint

    def generate_script(self, topic):
        headers = {'Authorization': f'Bearer {self.api_key}', 'Content-Type': 'application/json'}
        payload = {'topic': topic}

        response = requests.post(self.api_url, json=payload, headers=headers)

        if response.status_code == 200:
            return response.json().get('script', 'No script found')
        else:
            return f'Error: {response.status_code} - {response.text}'

# Example usage:
if __name__ == '__main__':
    api_key = 'your_gemini_api_key'  # Replace with your actual Gemini API key
    generator = ScriptGenerator(api_key)
    topic = 'How to integrate Gemini API for script generation'
    script = generator.generate_script(topic)
    print(script)