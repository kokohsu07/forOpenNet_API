API_KEY = '8c92e25b41b13c5a07ab566880d49580'
INVALID_API_KEY = 'test'
EMPTY_API_KEY = ''
BASE_URL_VALIDATION = 'http://apilayer.net/api/validate'
BASE_URL_COUNTRY = 'https://apilayer.net/api/countries'
RETRY_TIMES = 10
REQUEST_ACCESS_KEY = 'access_key'
REQUEST_NUMBER = 'number'
RESPONSE_ERROR = 'error'
RESPONSE_CODE = 'code'
RESPONSE_INFO = 'info'
RESPONSE_TYPE = 'type'
RESPONSE_COUNTRY_NAME='country_name'
RESPONSE_DIALLING_CODE='dialling_code'
EXPECT_TYPE_MSG_101_MISS = 'missing_access_key'
EXPECT_TYPE_MSG_101_INVALID = 'invalid_access_key'
EXPECT_TYPE_MSG_210 = 'no_phone_number_provided'
EXPECT_TYPE_MSG_211 = 'non_numeric_phone_number_provided'
EXPECT_HTTP_CODE_200 = 200
ERROR_CODE={'Auth':101,
            'empty_phone_number':210,
            'non_numeric_phone_number':211,
            'rate_limit_reached':106
            }