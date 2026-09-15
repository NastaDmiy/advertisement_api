# Файл test_api.py для тестирования

import requests
import json

BASE_URL = 'http://localhost:5000'


def test_create_ad():
    # Создание объявления
    data = {
        'title': 'Продам квартиру',
        'description': '3-комнатная квартира в центре города',
        'owner': 'Иван Петров'
    }

    response = requests.post(f'{BASE_URL}/advertisements', json=data)
    print('Create:', response.status_code, response.json())
    return response.json().get('id')


def test_get_ad(ad_id):
    # Получение объявления
    response = requests.get(f'{BASE_URL}/advertisements/{ad_id}')
    print('Get:', response.status_code, response.json())


def test_delete_ad(ad_id):
    # Удаление объявления
    response = requests.delete(f'{BASE_URL}/advertisements/{ad_id}')
    print('Delete:', response.status_code, response.json())


def test_get_all():
    # Получение всех объявлений
    response = requests.get(f'{BASE_URL}/advertisements')
    print('All ads:', response.status_code, len(response.json()), 'ads')


if __name__ == '__main__':
    # Тестирование
    ad_id = test_create_ad()
    if ad_id:
        test_get_ad(ad_id)
        test_get_all()
        test_delete_ad(ad_id)