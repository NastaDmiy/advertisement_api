import requests
import json

BASE_URL = 'http://127.0.0.1:5000'

# 1. Создаём объявление
print("1. Создание объявления:")
data = {
    'title': 'Продам квартиру',
    'description': '3-комнатная квартира в центре',
    'owner': 'Иван Петров'
}
r = requests.post(f'{BASE_URL}/advertisements', json=data)
print(f"   Статус: {r.status_code}")
ad = r.json()
print(json.dumps(ad, ensure_ascii=False, indent=2))
ad_id = ad['id']

# 2. Редактируем
print(f"\n2. Редактирование ID {ad_id}:")
update_data = {
    'title': 'Продам квартиру СРОЧНО',
    'owner': 'Пётр Сидоров'
}
r = requests.put(f'{BASE_URL}/advertisements/{ad_id}', json=update_data)
print(f"   Статус: {r.status_code}")
print(json.dumps(r.json(), ensure_ascii=False, indent=2))

# 3. Проверяем, что изменения применились
print(f"\n3. Получение после редактирования:")
r = requests.get(f'{BASE_URL}/advertisements/{ad_id}')
print(f"   Статус: {r.status_code}")
print(json.dumps(r.json(), ensure_ascii=False, indent=2))

# 4. Удаляем
print(f"\n4. Удаление:")
r = requests.delete(f'{BASE_URL}/advertisements/{ad_id}')
print(f"   Статус: {r.status_code}")
print(json.dumps(r.json(), ensure_ascii=False))