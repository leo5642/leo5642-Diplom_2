## Дипломный проект. Задание 2: Автотесты для API

### Автотесты для проверки API, которая отправляет запросы API в Stellar Burgers

### Реализованные сценарии

Созданы Автотесты для API, покрывающие ручки API  `api/auth/register`, 'api/auth/login', 'api/orders'.


### Структура проекта
- `allure-results` - Папка с отчетами 
- `locators` - Папка с данными для тестирования и URL
- `tests` - пакет, содержащий тесты. 
- `conftest` - файл с конфикстурами
### Запуск автотестов
putest

**Установка зависимостей**

> `$ pip install -r requirements.txt`
**Запуск автотестов и создание Allure-отчета**

>  `pytest --alluredir=./allure-results`
**Запуск Allure-отчета**
   `allure open ./allure-report`