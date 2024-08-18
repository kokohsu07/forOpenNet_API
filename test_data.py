from config import *

test_data_validation_phone_number = [
    (API_KEY, '14155552671', True),
    (API_KEY, '+14155552671', True),
    (API_KEY, '14155', False),
    (API_KEY, '', False),
    (API_KEY, 'AA', False),
    (INVALID_API_KEY, '14155552671', False),
    (EMPTY_API_KEY,'14155552671', False)
]

test_data_list_of_countries = [
    (API_KEY, 'AF', 'Afghanistan', '+93'),
    (API_KEY, 'AL', 'Albania', '+355'),
    (API_KEY, 'DZ', 'Algeria', '+213'),
    (INVALID_API_KEY, 'DZ', 'Algeria', '+213'),
    (EMPTY_API_KEY, 'DZ', 'Algeria', '+213')
]