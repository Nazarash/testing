import pytest
import requests

def check_url(url):
    response = requests.get(url)
    assert response.status_code == 200

    return response.json()


url_for_tests = [
    
    "https://dog.ceo/api/breeds/list/all",
    "https://dog.ceo/api/breeds/image/random",
    "https://dog.ceo/api/breeds/image/random/3",
    "https://dog.ceo/api/breed/hound/images/random/3",
    "https://dog.ceo/api/breed/hound/images",
    "https://dog.ceo/api/breed/hound/images/random",
    "https://dog.ceo/api/breed/hound/list",
    "https://dog.ceo/api/breed/hound/afghan/images",
    "https://dog.ceo/api/breed/hound/afghan/images/random/3",
    "https://dog.ceo/api/breed/hound/afghan/images/random",
]

answer_test = []

@pytest.mark.parametrize('url',url_for_tests)
def test_url(url):
    respons = check_url(url)
    answer_test.append((url,respons))

def test_result_test():
    with open('result_test.txt', "w", encoding="utf8") as result:
        for element in answer_test:
            answer = f'Ссылка: {element[0]}\n\n результат:\n {element[1]}\n\n'
            result.write(answer)

