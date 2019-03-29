# import libraries
 
import requests
import json
 
# prepare the parameters
# replace {starting date} and {ending date} with the timeframes needed
# replace {email address} with your Contentful email address and {API token} from Contentful admin section
 
url = 'https://contentful.zendesk.com/api/v2/search.json?query=type:ticket status:solved status:closed created>=2019-01-01 created<2019-03-31'
headers = {'Authorization':'Basic ZmFqcmkuaGFu_bnlAY29udGVudGZ1bC5jb20vdG9rZW46dDA4VjVSSEVvSHFIejVNZG9GVmVaYUdZd2J1Mnh0M2FsNTduM0ZsbA=='}
 
# open the file
fo = open("ticket_id.txt","a+")
 
while url:
 
    # request for the data
    response = requests.get(url,headers=headers)
 
    # convert the response into json
    data = response.json()
 
    # convert the json formatted response into a string
    data_string =json.dumps(data)
 
    # to be able to traverse the JSON arrays
    data_dump = json.loads(data_string)
 
    limit = len(data_dump['results'])
 
    for index in range(0,limit):
        fo.write(str(data_dump['results'][index]['id']))
        fo.write("\n")
 
    url = data_dump['next_page']
    print(url)
 
else:
    fo.close()