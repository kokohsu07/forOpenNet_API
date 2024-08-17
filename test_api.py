import pytest
import requests
from config import *

@pytest.mark.parametrize("phone_number, expected_valid", [
    ('14155552671', True),
    ('+14155552671', True),
    ('14155', False) #Invalid Phone Number
])
def test_numverify_validation_phone_number(phone_number, expected_valid):
    params = {
        'access_key': API_KEY,
        'number': phone_number
    }
    response = requests.get(BASE_URL_VALIDATION, params=params)
    data = response.json()
    while 'error' in data and data['error']['type']=='rate_limit_reached':
        response = requests.get(BASE_URL_VALIDATION, params=params)
        data = response.json()

    assert response.status_code == 200
    assert data['valid'] == expected_valid


@pytest.mark.parametrize("country_code, expect_country_name, expect_dialling_code", [
    ('AF', 'Afghanistan', '+93'),
    ('AL', 'Albania', '+355'),
    ('DZ', 'Algeria', '+213')
])
def test_numverify_list_of_countries(country_code, expect_country_name, expect_dialling_code):
    params = {
        'access_key': API_KEY,
    }
    response = requests.get(BASE_URL_COUNTRY, params=params)
    data = response.json()

    while 'error' in data :
         response = requests.get(BASE_URL_COUNTRY, params=params)
         data = response.json()
    assert response.status_code == 200
    assert data[country_code]['country_name'] == expect_country_name
    assert data[country_code]['dialling_code'] == expect_dialling_code


if __name__ == "__main__":
    pytest.main()
