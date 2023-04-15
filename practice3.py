import requests
import json

# Виконати запит на API та отримати відповідь
response = requests.get('https://api.exchangeratesapi.io/latest')

# Декодувати відповідь у форматі JSON
data = json.loads(response.text)

# Обробити та проаналізувати дані
rates = data['rates']
eur_rate = rates['EUR']
usd_rate = rates['USD']

# Зберегти дані у форматі JSON на локальному пристрої
with open('rates.json', 'w') as f:
    json.dump(rates, f)

# Відобразити дані у зручному для користувача вигляді
print(f'1 EUR = {eur_rate:.2f} USD')
print(f'1 USD = {1/usd_rate:.2f} EUR')
