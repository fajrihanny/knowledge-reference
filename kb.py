# import libraries
 
import requests
import json
 
# preps the parameters
# replace {email address} with your Contentful email address and {API token} from Contentful admin section
 
headers = {'Authorization':'Basic Base64-encoded-of{email address}:{API token}'}
infile = open ("ticket_id.txt","r")
KBtickets = open ("KB_tickets.txt", "a")
tickets_solved = 0
tickets_solved_with_KB = 0
 
for ticketId in infile:
    try:
        url = 'https://contentful.zendesk.com/api/v2/tickets/'+ticketId+'/comments.json'
        tickets_solved += 1
        response = requests.get(url,headers=headers)
        data = response.json()
        data_string = json.dumps(data)
        data_dump = json.loads(data_string)
        if 'comments' in data_dump:
            limit = len(data_dump['comments'])
            for index in range (0,limit):
                if "https://www.contentful.com/developers/docs/" in (data_dump['comments'][index]['body']):
                    KBtickets.write("Ticket ID: "+ticketId+"\n")
                    tickets_solved_with_KB += 1
                    break
        else:
            print("Ticket ID: "+ticketId+" doesn't have comments")
    except Exceptions:
        print("Ticket ID = "+ticketId+" has exceptions")
        pass
 
KBtickets.write("Tickets solved = "+str(tickets_solved))
KBtickets.write("\n")
KBtickets.write("Tickets solved with Documentations = "+str(tickets_solved_with_KB))
KBtickets.close()
infile.close()
