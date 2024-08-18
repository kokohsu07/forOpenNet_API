API - Validation Phone Number 
| test case  |  expected result  |  expected result  |
| ------------- | ------------- | ------------- |
| [API][Validation_Phone_Number] Input valid phone number with all number  | The API should getting 200 and the parameter of 'valid' should be True  | Positive |
| [API][Validation_Phone_Number] Input valid phone number with plus code and number  | The API should getting 200 and the parameter of 'valid' should be True | Postive |
| [API][Validation_Phone_Number] Input invalid phone number with less number  | The API should getting 200 and the parameter of 'valid' should be False | Negative |
| [API][Validation_Phone_Number] Input invalid phone number with empty  | The API should getting 200 and the error type should be 'no_phone_number_provided' | Negative |
| [API][Validation_Phone_Number] Input invalid phone number with all alphabet | The API should getting 200 and the error type should be 'non_numeric_phone_number_provided' | Negative |
| [API][Validation_Phone_Number] Input invalid access key with incorrect key | The API should getting 200 and the error type should be 'invalid_access_key' | Negative |
| [API][Validation_Phone_Number] Input invalid access key with empty key | The API should getting 200 and the error type should be 'missing_access_key' | Negative |


API - List of Countries
| test case  |  expected result  |  expected result  |
| ------------- | ------------- | ------------- |
| [API][Validation_Phone_Number] Input valid access key and pick some of JSON data to do the validation  | The API should getting 200 and the corresponding data shoule be correct | Positive |
| [API][Validation_Phone_Number] Input invalid access key with incorrect key | The API should getting 200 and the error type should be 'invalid_access_key' | Negative |
| [API][Validation_Phone_Number] Input invalid access key with empty key | The API should getting 200 and the error type should be 'missing_access_key' | Negative |



