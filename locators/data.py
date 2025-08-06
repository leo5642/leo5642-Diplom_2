import pytest
import requests
import random
import string

class AuthData():
    login = [
        ("login", "Недостаточно данных для создания учетной записи"),
        ("password", "Недостаточно данных для создания учетной записи"),
    ]
    
    my_register = {
        "email": "leo5642@tets.ru",
        "password": "sdfsdfsdf",
        "name":  "leo5642"
    }

    my_login = {
        "email": "leo5642@tets.ru",
        "password": "sdfsdfsdf"
    }

    no_vlid_my_login = {
        "email": "leo5642@tets.ru123",
        "password": "sdfsdfsdf123"
        }


    my_order = {
        "ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa6f"]
    }

