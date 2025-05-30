# eteocatsapi

Небольшой веб сервис для получения погоды через API
Использует api сайтов:

- 2GIS: https://dev.2gis.ru/api
- open-meteo.com: https://open-meteo.com/

2GIS предоставляет получение latitude и longitude, что важно для дальнейшей работы
с сайтом open-meteo.com, который ожидает получения этих данных. Также 2GIS предоставляет API для автодополнения при
наборе населённых пунктов.

В файле .env.example находится уже готовый тестовый ключ для взаимодействия с API.

Помимо работы над получением данных и обработки в FastAPI у сервиса также есть простая связка с frontend написанным на Vue.js.
Для корректной работы не рекомендуется менять стандартный порт FastAPI(8123) поскольку Vue стучит на этот порт по адресу
http://localhost:8123/weather/{city}

FastAPI:
http://localhost:8123/weather/{city}

Vue.js
http://localhost:5174/

# запуск локально
1. создать файл .env
```bash
touch .env
```
2. скопировать в него содержимое из файла .env.example (мануально или командой в терминале)

```bash
cp .env.example .env
```

3. перейти в backend через cd и запустить pip install -r requirements.txt

```bash
cd backend
pip install -r requirements.txt
```

4. Не забудьте создать и активировать venv (через poetry или python)
5. Находясь в директории запустить python3 -m app (если мак) или python -m app(на других устройствах)

```bash
python3 -m app
```
FrontEnd локально
1. Для запуска фронтенда перейдите по пути /frontend/forecastapi
запустите:

1. npm run install
1. npm run build
2. npm run dev


[![asciicast](https://asciinema.org/a/bIptFyga6eHvSzQ5weKqunULX.svg)](https://asciinema.org/a/bIptFyga6eHvSzQ5weKqunULX)


Для запуска приложения из докера

1. создайте и заполните .env файл по той же инструкции, что и для локального сервера
2. запустите docker-compose build из root директории 
3. Дождавшись загрузки образа напишите docker-compose up
4. после поднятия сервера перейдите на соответсвующий адрес, если вы не меняли порт, то стандартным будет адрес
   
1. http://0.0.0.0:8123/        - backend сервис.
2. http://0.0.0.0:8123/docs    - backend документация.
3. http://0.0.0.0:8123/weather/{city}  - адрес сервиса погоды.
Для тестирования советую использовать /docs вкладку fastapi и протестировать данные через openapi
# запуск Docker
