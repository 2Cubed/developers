import requests
import sys

s = requests.Session()

login_response = s.post('https://beam.pro/api/v1/users/login', data={
    'username': sys.argv[1],
    'password': sys.argv[2]
})
