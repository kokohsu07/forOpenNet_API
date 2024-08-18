import logging
import pytest
import requests
from config import *
from test_data import *

LOGGER = logging.getLogger(__name__)

@pytest.mark.parametrize("api_key, phone_number, expected_valid", test_data_validation_phone_number)
def test_numverify_validation_phone_number(api_key, phone_number, expected_valid):
    params = {
        REQUEST_ACCESS_KEY : api_key,
        REQUEST_NUMBER: phone_number
    }
    response = requests.get(BASE_URL_VALIDATION, params=params)
    data = response.json()
    try:
        assert response.status_code == EXPECT_HTTP_CODE_200
    except:
        LOGGER.error(response.status_code)

    if RESPONSE_ERROR in data:
        try:
            error_code=data[RESPONSE_ERROR][RESPONSE_CODE]
            error_info=data[RESPONSE_ERROR][RESPONSE_INFO]
            error_type=data[RESPONSE_ERROR][RESPONSE_TYPE]
        except:
            pass

        if error_code == ERROR_CODE['Auth']:
            if not api_key:
                assert error_type == EXPECT_TYPE_MSG_101_MISS, error_info
            else:
                assert error_type == EXPECT_TYPE_MSG_101_INVALID, error_info

        elif error_code == ERROR_CODE['empty_phone_number']:
            assert data[RESPONSE_ERROR][RESPONSE_TYPE] == EXPECT_TYPE_MSG_210, error_info

        elif error_code == ERROR_CODE['non_numeric_phone_number']:
            assert data[RESPONSE_ERROR][RESPONSE_TYPE] == EXPECT_TYPE_MSG_211, error_info

        elif error_code == ERROR_CODE['rate_limit_reached']:
            for i in range(RETRY_TIMES):
                if RESPONSE_ERROR in data and error_code == ERROR_CODE['rate_limit_reached']:
                    response = requests.get(BASE_URL_VALIDATION, params=params)
                    data = response.json()
                    try:
                        error_code = data[RESPONSE_ERROR][RESPONSE_CODE]
                    except:
                        pass
                elif RESPONSE_ERROR not in data:
                    break
        LOGGER.info("\nERROR MESSAGE : " + error_info)

    if RESPONSE_ERROR not in data:
        assert data['valid'] == expected_valid



@pytest.mark.parametrize("api_key, country_code, expect_country_name, expect_dialling_code", test_data_list_of_countries)
def test_numverify_list_of_countries(api_key, country_code, expect_country_name, expect_dialling_code):
    params = {
        REQUEST_ACCESS_KEY : api_key,
    }
    response = requests.get(BASE_URL_COUNTRY, params=params)
    data = response.json()
    try:
        assert response.status_code == EXPECT_HTTP_CODE_200
    except:
        LOGGER.error(response.status_code)


    if RESPONSE_ERROR in data:
        try:
            error_code = data[RESPONSE_ERROR][RESPONSE_CODE]
            error_info = data[RESPONSE_ERROR][RESPONSE_INFO]
            error_type = data[RESPONSE_ERROR][RESPONSE_TYPE]
        except:
            pass


        if error_code == ERROR_CODE['Auth']:
            if not api_key:
                assert error_type == EXPECT_TYPE_MSG_101_MISS, error_info
            else:
                assert error_type == EXPECT_TYPE_MSG_101_INVALID, error_info

        elif error_code == ERROR_CODE['rate_limit_reached']:
            for i in range(RETRY_TIMES):
                if RESPONSE_ERROR in data and error_code == ERROR_CODE['rate_limit_reached']:
                    response = requests.get(BASE_URL_VALIDATION, params=params)
                    data = response.json()
                    try:
                        error_code=data[RESPONSE_ERROR][RESPONSE_CODE]
                    except:
                        pass
                else:
                    break
        LOGGER.info("\nERROR MESSAGE : " + error_info)

    if RESPONSE_ERROR not in data:
        assert data[country_code][RESPONSE_COUNTRY_NAME] == expect_country_name
        assert data[country_code][RESPONSE_DIALLING_CODE] == expect_dialling_code


if __name__ == "__main__":
    pytest.main()
