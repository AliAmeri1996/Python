import requests

parameters={"amount":10,"type":"boolean"}# amount and type are parameters that we have changed.


response=requests.get("https://opentdb.com/api.php",params=parameters)#https://opentdb.com/api.php?amount=10&type=boolean this is the whole api url but the endpoint is
#everything before the "?", anything after are parameters....later we can add the parameters as we have done.
response.raise_for_status()
data=response.json()
question_data=(data["results"])#we are only interested in the results section


