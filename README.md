# eteocatsapi

Небольшой веб сервис для получения погоды через API
Использует api сайтов:

- 2GIS: https://dev.2gis.ru/api
- open-meteo.com: https://open-meteo.com/

2GIS предоставляет получение latitude и longitude, что важно для дальнейшей работы
с сайтом open-meteo.com, который ожидает получения этих данных. Также 2GIS предоставляет API для автодополнения при
наборе населённых пунктов.

В файле .env находится уже готовый тестовый ключ для взаимодействия с API.

Помимо работы над получением данных и обработки в FastAPI у сервиса также есть простая связка с frontend написанным на Vue.js.
Для корректной работы не рекомендуется менять стандартный порт FastAPI(8123) поскольку Vue стучит на этот порт по адресу
http://localhost:8123/weather/{city}

FastAPI:
http://localhost:8123/weather/{city}

Vue.js
http://localhost:5174/

# запуск локально

[![asciicast](https://asciinema.org/a/bIptFyga6eHvSzQ5weKqunULX.svg)](https://asciinema.org/a/bIptFyga6eHvSzQ5weKqunULX)

Вне зависимости от выбранного метода вам нужно создать файл .env и заполнить его данными по примеру данных из .env.example

1. только fastapi
   1.1 установите poetry следуя инструкциям на официальном сайте
2. перейдите в backend
3. установите зависимости для poetry
4. перейдите из корневой директории по пути backend/app/
5. запустите команду python __main__.py

Если всё прошло успешно вы увидите сообщение о запуске
2. fastapi+vue.js

1. проделайте все шаги как и для fastapi
2. перейдите в директорию frontend/forecastapi
3. запустите npm install
4. запустите npm run dev

Если всё прошло успешно вы увидте сообщение о запущенном порте
http://localhost:5174/

# запуск Docker
