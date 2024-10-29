# In this file, we will have our utils functions 

## Apache Airflow

### Fetching Data and formattingIt
import requests
def fetch_data():
    import requests
    
    # Getting back the response from the request
    res = requests.get("https://randomuser.me/api/")
    res = res.json()['results'][0]
    
    return res
    
# Now, the respone has too many info, we need to extract the ones whe truly need
def format_data(res):
    data = {}
    data['first_name'] = res['name']['first']
    data['last_name'] = res['name']['last']
    data['address'] = str(res['location']['street']['name'] + ' ,' + res['location']['city'] + ' ,' + res['location']['state'] + ' ,' + res['location']['country'])
    data['email'] = res['email']
    data['username'] = res['login']['username']
    data['dob'] = res['dob']['date']
    data['phone'] = res['phone']
    data['profile_pic'] = res['picture']['medium']
    data['nationality'] = res['nat']
    
    return data