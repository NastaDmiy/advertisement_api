import requests
import json

BASE_URL = 'http://127.0.0.1:5000'

def test_create():
    print("1. Создание объявления...")
    data = {
        'title': 'Продам квартиру',
        'description': '3-комнатная квартира в центре',
        'owner': 'Иван Петров'
    }
    response = requests.post(f'{BASE_URL}/advertisements', json=data)
    print(f"   Статус: {response.status_code}")
    print(f"   Ответ: {json.dumps(response.json(), ensure_ascii=False, indent=2)}")
    return response.json().get('id')

def test_get_all():
    print("\n2. Получение всех объявлений...")
    response = requests.get(f'{BASE_URL}/advertisements')
    print(f"   Статус: {response.status_code}")
    ads = response.json()
    print(f"   Всего: {len(ads)}")
    for ad in ads:
        print(f"   - ID {ad['id']}: {ad['title']} ({ad['owner']})")

def test_get_one(ad_id):
    print(f"\n3. Получение объявления ID {ad_id}...")
    response = requests.get(f'{BASE_URL}/advertisements/{ad_id}')
    print(f"   Статус: {response.status_code}")
    print(f"   Ответ: {json.dumps(response.json(), ensure_ascii=False, indent=2)}")

def test_delete(ad_id):
    print(f"\n4. Удаление объявления ID {ad_id}...")
    response = requests.delete(f'{BASE_URL}/advertisements/{ad_id}')
    print(f"   Статус: {response.status_code}")
    print(f"   {response.json()}")

if __name__ == '__main__':
    ad_id = test_create()
    if ad_id:
        test_get_all()
        test_get_one(ad_id)
        # test_delete(ad_id)
    print("\n Готово!")