import requests
import pprint
import json

# создать свои запросы для сущностей тестируемого API (по 4 запроса) user и store
# по базовому url с реализацией базового класса 
# тестирования(пример приведен в репозитории)


class BaseRequest:
    def __init__(self, base_url):
        self.base_url = base_url
        # set headers, authorisation etc

    def _request(self, url, request_type, data=None, expected_error=False):
        stop_flag = False
        headers = {'content-type': 'application/json','api_key': 'ITHUB'}

        if data:
            data = json.dumps(data)

        while not stop_flag:
            if request_type == 'GET':
                response = requests.get(url, headers=headers)
            elif request_type == 'POST':
                response = requests.post(url, data=data, headers=headers)
            elif request_type == 'PUT':
                response = requests.put(url, data=data, headers=headers)
            else:
                response = requests.delete(url)

            if not expected_error and response.status_code == 200:
                stop_flag = True
            elif expected_error:
                stop_flag = True

            pprint.pprint("Trying to connect..."+url)
            pprint.pprint(response.status_code)
            pprint.pprint(response.reason)
        pprint.pprint(f'{request_type} example')
        pprint.pprint(response.url)
        pprint.pprint(response.status_code)
        pprint.pprint(response.reason)
        pprint.pprint(response.text)
        pprint.pprint(response.json())
        pprint.pprint('**********')

        return response

    def get(self, endpoint, endpoint_id, expected_error=False):
        url = f'{self.base_url}/{endpoint}/{endpoint_id}'
        response = self._request(url, 'GET', expected_error=expected_error)
        return response.json()

    def post(self, endpoint, endpoint_id, body):
        if endpoint_id == '':
            url = f'{self.base_url}/{endpoint}'
        else:
            url = f'{self.base_url}/{endpoint}/{endpoint_id}'
        response = self._request(url, 'POST', data=body)
        msg = response.json().get('message', None)
        return msg if msg is not None else response.json().get('id', 'ХЫЫЫЫЫЫЫ')

    def put(self, endpoint, endpoint_id, body):
        url = f'{self.base_url}/{endpoint}/{endpoint_id}'
        response = self._request(url, 'PUT', data=body)
        return response.json()['message']

    def delete(self, endpoint, endpoint_id):
        url = f'{self.base_url}/{endpoint}/{endpoint_id}'
        response = self._request(url, 'DELETE')
        return response.json()['message']


BASE_URL_PETSTORE = 'https://petstore.swagger.io/v2'
base_request = BaseRequest(BASE_URL_PETSTORE)


data1 = {"id": "1"}

data = {
    "id": 0,
    "username": "Ivan2004",
    "firstName": "Ivan",
    "lastName": "Saygin",
    "email": "ivan2004@mail.ru",
    "password": "asdada",
    "phone": "86359421545",
    "userStatus": 1
  }

# post user
user_id = base_request.post('user', '', data)
pprint.pprint(user_id)
pass

# post store 
store_id = base_request.post('store', "order", data1)
store_info = base_request.get('store/order',store_id)
pprint.pprint(store_info)
pass

# get 1 store
get_ferst_store = base_request.get('store/order', store_id)
pprint.pprint(get_ferst_store)
pass

# get 2 store 
get_second_store = base_request.get('store','inventory')
pprint.pprint(get_second_store)
pass

# delete store 
delete_id = base_request.delete('store/order', store_id)
delete_info = base_request.get('pet', delete_id)
pprint.pprint(delete_info)
pass

# get USER
user_info = base_request.get('user', 'login')
pprint.pprint(user_info)
pass


# delete USER
delete_user = base_request.delete('user', "Ivan2004")
pprint.pprint(delete_user)
pass


# put USER
data["phone"] = "85615478961"
user_put = base_request.put('user', "Ivan2004", data)
pprint.pprint(user_put)
pass
