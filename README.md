# test_tenafli_django

-> Clone the repository or unzip the zip file
-> Install the required dependencies : pip install -r requirements.txt or pip3 install -r requirements.txt
-> Start the Django development server : python3 manage.py runserver
-> Access the API endpoint by opening a web browser or using a tool like cURL or Postman : http://localhost:8000/api/top-5-states/

__ The final results in json by the api depends on (samples) 20 schools retrieved from each state which are not static but retrieved dynamically on each request.
__ The appID and the appKey used are from my account.
__ If getting internal error 500 when calling the api , wait a few minutes and retry (it depends on https://api.schooldigger.com/ response).