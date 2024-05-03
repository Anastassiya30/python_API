import json
import random
import uuid

import requests


# from requests_toolbalt.multipart.encoder import MultipartEncoder


class Pets:
    # ***API библиотека к сайту http://34.141.58.52:8080/#/***

    def __init__(self):
        self.base_url = "http://34.141.58.52:8000/"

    def post_register(self):
        """Запрос к Swagger сайта для регистрации пользователя"""
        e = uuid.uuid4().hex
        data = {"email": f'{e}@mail.com',
                "password": '1234',
                "confirm_password": '1234'}
        res = requests.post(self.base_url + "register", data=json.dumps(data))
        status = res.status_code
        return status

    def get_token(self) -> json:
        """Запрос к Swagger сайта для получения уникального токена пользователя по указанным email и password"""
        data = {"email": "user@mail.com",
                "password": "1234"}
        res = requests.post(self.base_url + "login", data=json.dumps(data))
        my_token = res.json()["token"]
        my_id = res.json()["id"]
        status = res.status_code
        return my_token, status, my_id

    def get_user_id(self):
        """Запрос к Swagger сайта для получения id пользователя """
        my_token = Pets().get_token()[0]
        headers = {"Authorization": f'Bearer {my_token}'}
        res = requests.get(self.base_url + "users", headers=headers)
        status = res.status_code
        my_id = res.text
        return status, my_id

    def post_pet(self):
        """Запрос к Swagger сайта для создания нового питомца """
        my_token = Pets().get_token()[0]
        my_id = Pets().get_token()[2]
        headers = {"Authorization": f'Bearer {my_token}'}
        data = {"id": my_id,
                "name": 'new one', "type": 'dog', "age": 0, "owner_id": my_id}
        res = requests.post(self.base_url + 'pet', data=json.dumps(data), headers=headers)
        pet_id = res.json()['id']
        status = res.status_code
        return pet_id, status

    def post_pet_list(self):
        """"Запрос к Swagger сайта для получения списка питомцев"""
        my_token = Pets().get_token()[0]
        my_id = Pets().get_token()[2]
        headers = {"Authorization": f'Bearer {my_token}'}
        data = {"user_id": my_id}
        res = requests.post(self.base_url + 'pets', data=json.dumps(data), headers=headers)
        status = res.status_code
        return status

    def get_pet_photo(self):
        """Запрос к Swagger сайта для загрузки фото для созданного питомца """
        my_token = Pets().get_token()[0]
        pet_id = Pets().post_pet()[0]
        headers = {"Authorization": f'Bearer {my_token}'}
        files = {'pic': (
            'Yellow_Mongoose.jpg',
            open('C:\\Users\\Anast\\PycharmProjects\\python_API\\photo\\Yellow_Mongoose.jpg', 'rb'),
            'image/jpg')}
        res = requests.post(self.base_url + f'pet/{pet_id}/image', headers=headers, files=files)
        status = res.status_code
        link = res.json()['link']
        return status, link

    def patch_pet(self):
        """Запрос к Swagger сайта для обновления данных питомца """
        my_token = Pets().get_token()[0]
        my_id = Pets().get_token()[2]
        pet_id = Pets().post_pet()[0]
        headers = {"Authorization": f'Bearer {my_token}'}
        data = {"id": pet_id,
                "name": 'Yeter', "type": 'reptile', "owner_id": my_id}
        res = requests.patch(self.base_url + "pet", data=json.dumps(data), headers=headers)
        status = res.status_code
        return status, pet_id

    def put_pet_like(self):
        """Запрос к Swagger сайта для того, чтобы поставить лайк питомцу """
        my_token = Pets().get_token()[0]
        headers = {"Authorization": f'Bearer {my_token}'}
        pet_id = Pets().post_pet()[0]
        res = requests.put(self.base_url + f"pet/{pet_id}/like", headers=headers)
        status = res.status_code
        return pet_id, status

    def delete_pet(self):
        """Запрос к Swagger сайта для удаления питомца """
        my_token = Pets().get_token()[0]
        headers = {"Authorization": f'Bearer {my_token}'}
        pet_id = Pets().post_pet()[0]
        res = requests.delete(self.base_url + f'pet/{pet_id}', headers=headers)
        status = res.status_code
        return pet_id, status


Pets().post_register()
Pets().get_token()
Pets().get_user_id()
Pets().post_pet()
Pets().post_pet_list()
Pets().get_pet_photo()
Pets().patch_pet()
Pets().put_pet_like()
Pets().delete_pet()

