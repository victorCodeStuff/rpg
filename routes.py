from flask import request
from llm import completion

def routes_setup(app):
    @app.post('/api')
    def create_data():
        request_data = request.get_json()
        data = request_data['user_prompt']
        response = completion(data)
        print(response.choices[0].message.content)
        return ""
