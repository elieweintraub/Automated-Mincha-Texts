import requests

API_URL = 'http://jservice.io/api/random'

def get_question():
    try:
        response = requests.get(API_URL)
        if (response.status_code == 200):
            json_response= response.json()[0]
            category = json_response['category']['title']
            question = json_response['question']
            answer = json_response['answer']
            return (category, question, answer)
    except:
        pass
    return None
